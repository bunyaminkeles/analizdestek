from django.core.mail import send_mail
from django.conf import settings
import threading

def send_email_async(subject, message, recipient_list):
    """
    Email gönderimini arka planda thread ile yapar (timeout olmaz)
    """
    def _send():
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=recipient_list,
                fail_silently=True,
                timeout=10,  # 10 saniye timeout
            )
            print(f"✅ Email gönderildi: {recipient_list}")
        except Exception as e:
            print(f"❌ Email gönderim hatası: {e}")
    
    # Thread'i başlat ve arka plana at
    thread = threading.Thread(target=_send)
    thread.daemon = True  # Ana program kapanınca thread de kapansın
    thread.start()


def send_topic_reply_notification(post, topic):
    """
    Bir konuya cevap yazıldığında konu sahibine email gönderir
    """
    # Kendi mesajına cevap yazıyorsa bildirim gönderme
    if post.created_by == topic.starter:
        return
    
    # Konu sahibinin email'i yoksa veya bildirim kapalıysa gönderme
    if not topic.starter.email:
        return
    
    # Kullanıcı tercihini kontrol et
    if hasattr(topic.starter, 'profile') and not topic.starter.profile.email_on_reply:
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
    # Alıcının email'i yoksa veya bildirim kapalıysa gönderme
    if not receiver.email:
        return
    
    # Kullanıcı tercihini kontrol et
    if hasattr(receiver, 'profile') and not receiver.profile.email_on_private_message:
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