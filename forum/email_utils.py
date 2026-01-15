from django.conf import settings
import logging
import threading
import os

# SendGrid Web API kullan (SMTP yerine - Render'da SMTP engellenmiş olabilir)
try:
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail, Email, To, Content
    SENDGRID_AVAILABLE = True
except ImportError:
    SENDGRID_AVAILABLE = False

logger = logging.getLogger(__name__)

def send_email_async(subject, message, recipient_list):
    """
    Email gönderimini arka planda thread ile yapar (request timeout olmasın)
    SendGrid Web API kullanır (SMTP yerine - daha güvenilir)
    """
    logger.info(f"📧 Email gönderme başlıyor: {recipient_list}")
    print(f"📧 Email gönderme başlıyor: {recipient_list}")

    def _send():
        try:
            if not SENDGRID_AVAILABLE:
                logger.error("❌ SendGrid kütüphanesi yüklü değil!")
                print("❌ SendGrid kütüphanesi yüklü değil!")
                return

            api_key = os.getenv('SENDGRID_API_KEY', '')
            if not api_key:
                logger.error("❌ SENDGRID_API_KEY tanımlı değil!")
                print("❌ SENDGRID_API_KEY tanımlı değil!")
                return

            from_email = settings.DEFAULT_FROM_EMAIL
            logger.info(f"📤 SendGrid Web API ile gönderiliyor...")
            print(f"📤 SendGrid Web API ile gönderiliyor...")
            logger.info(f"🔍 FROM_EMAIL: {from_email}")
            print(f"🔍 FROM_EMAIL: {from_email}")
            logger.info(f"🔍 TO_EMAILS: {recipient_list}")
            print(f"🔍 TO_EMAILS: {recipient_list}")

            # SendGrid Mail objesi oluştur ve gönder
            sg = SendGridAPIClient(api_key)

            for recipient in recipient_list:
                mail = Mail(
                    from_email=from_email,
                    to_emails=recipient,
                    subject=subject,
                    plain_text_content=message
                )

                # API ile gönder
                response = sg.send(mail)

                logger.info(f"✅ Email gönderildi: {recipient} (Status: {response.status_code})")
                print(f"✅ Email gönderildi: {recipient} (Status: {response.status_code})")

                if response.status_code != 202:
                    logger.warning(f"⚠️ Beklenmedik status code: {response.status_code}")
                    print(f"⚠️ Beklenmedik status code: {response.status_code}")

        except Exception as e:
            logger.error(f"❌ Email gönderim hatası: {e}", exc_info=True)
            print(f"❌ Email gönderim hatası: {e}")
            print(f"❌ Hata tipi: {type(e).__name__}")
            print(f"❌ Hata detayı: {str(e)}")
            import traceback
            traceback.print_exc()

    # Thread'de arka planda gönder
    thread = threading.Thread(target=_send)
    thread.daemon = False
    thread.start()
    logger.info(f"🔄 Email thread başlatıldı (SendGrid Web API)")
    print(f"🔄 Email thread başlatıldı (SendGrid Web API)")


def send_topic_reply_notification(post, topic):
    """
    Bir konuya cevap yazıldığında konu sahibine email gönderir
    """
    logger.info(f"🔔 Email bildirim kontrolü: {post.created_by.username} -> Topic #{topic.pk} (Sahibi: {topic.starter.username})")
    print(f"🔔 Email bildirim kontrolü: {post.created_by.username} -> Topic #{topic.pk} (Sahibi: {topic.starter.username})")

    # Kendi mesajına cevap yazıyorsa bildirim gönderme
    if post.created_by == topic.starter:
        logger.info(f"⚠️ Email gönderilmedi: Kullanıcı kendi konusuna cevap yazdı ({post.created_by.username})")
        print(f"⚠️ Email gönderilmedi: Kullanıcı kendi konusuna cevap yazdı ({post.created_by.username})")
        return

    # Konu sahibinin email'i yoksa veya bildirim kapalıysa gönderme
    if not topic.starter.email:
        logger.warning(f"⚠️ Email gönderilmedi: Konu sahibinin email adresi yok ({topic.starter.username})")
        print(f"⚠️ Email gönderilmedi: Konu sahibinin email adresi yok ({topic.starter.username})")
        return

    # Kullanıcı tercihini kontrol et
    if hasattr(topic.starter, 'profile') and not topic.starter.profile.email_on_reply:
        logger.info(f"⚠️ Email gönderilmedi: Kullanıcı email bildirimlerini kapattı ({topic.starter.username})")
        print(f"⚠️ Email gönderilmedi: Kullanıcı email bildirimlerini kapattı ({topic.starter.username})")
        return
    
    subject = f"🔔 {post.created_by.username} konunuza cevap yazdı: {topic.subject}"
    
    message = f"""
Merhaba {topic.starter.username},

"{topic.subject}" başlıklı konunuza yeni bir cevap geldi!

Cevap Yazan: {post.created_by.username}
Mesaj: {post.message[:200]}...

Cevabın tamamını görmek için:
https://analizdestek-ai.onrender.com/topic/{topic.pk}/

---
Bu bir otomatik bildirimdir. Cevap vermek için siteye giriş yapın.
AnalizDestek - Akademik Veri Üssü
"""
    
    # Asenkron gönder (timeout olmaz)
    send_email_async(subject, message, [topic.starter.email])


def send_private_message_notification(sender, receiver, message_content):
    """
    Özel mesaj geldiğinde alıcıya email gönderir
    """
    logger.info(f"💌 Özel mesaj email kontrolü: {sender.username} -> {receiver.username}")
    print(f"💌 Özel mesaj email kontrolü: {sender.username} -> {receiver.username}")

    # Alıcının email'i yoksa veya bildirim kapalıysa gönderme
    if not receiver.email:
        logger.warning(f"⚠️ Özel mesaj email gönderilmedi: Alıcının email adresi yok ({receiver.username})")
        print(f"⚠️ Özel mesaj email gönderilmedi: Alıcının email adresi yok ({receiver.username})")
        return

    # Kullanıcı tercihini kontrol et
    if hasattr(receiver, 'profile') and not receiver.profile.email_on_private_message:
        logger.info(f"⚠️ Özel mesaj email gönderilmedi: Kullanıcı bildirimleri kapattı ({receiver.username})")
        print(f"⚠️ Özel mesaj email gönderilmedi: Kullanıcı bildirimleri kapattı ({receiver.username})")
        return
    
    subject = f"💌 {sender.username} size özel mesaj gönderdi"
    
    message = f"""
Merhaba {receiver.username},

{sender.username} size yeni bir özel mesaj gönderdi!

Mesaj İçeriği:
{message_content[:300]}...

Mesajı okumak ve cevaplamak için:
https://analizdestek-ai.onrender.com/inbox/

---
Bu bir otomatik bildirimdir.
AnalizDestek - Akademik Veri Üssü
"""
    
    # Asenkron gönder (timeout olmaz)
    send_email_async(subject, message, [receiver.email])


def send_mention_notification(mentioned_user, post, topic):
    """
    Bir mesajda mention edildiğinde kullanıcıya email gönderir
    (İsteğe bağlı - gelecekte @username özelliği için)
    """
    if not mentioned_user.email:
        return
    
    subject = f"👋 {post.created_by.username} sizi bir tartışmada bahsetti"
    
    message = f"""
Merhaba {mentioned_user.username},

{post.created_by.username} sizi "{topic.subject}" konusunda bahsetti!

Konuya gitmek için:
https://analizdestek-ai.onrender.com/topic/{topic.pk}/

---
AnalizDestek - Akademik Veri Üssü
"""
    
    # Asenkron gönder (timeout olmaz)
    send_email_async(subject, message, [mentioned_user.email])