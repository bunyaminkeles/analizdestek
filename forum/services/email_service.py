"""
E-posta gönderme servisi
"""
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.urls import reverse
import logging

logger = logging.getLogger(__name__)


class EmailService:
    """E-posta gönderme işlemlerini yöneten servis"""

    @staticmethod
    def is_configured():
        """E-posta ayarlarının yapılandırılıp yapılandırılmadığını kontrol eder"""
        return bool(getattr(settings, 'EMAIL_HOST_PASSWORD', ''))

    @staticmethod
    def get_base_url():
        """Site URL'sini döndürür"""
        return getattr(settings, 'SITE_URL', 'http://localhost:8000')

    @classmethod
    def send_verification_email(cls, user, verification_token):
        """
        Kullanıcıya e-posta doğrulama linki gönderir

        Args:
            user: User modeli instance
            verification_token: EmailVerification modeli instance

        Returns:
            bool: Gönderim başarılı mı
        """
        verification_url = f"{cls.get_base_url()}/verify-email/{verification_token.token}/"

        context = {
            'user': user,
            'verification_url': verification_url,
            'site_name': 'Analizus',
            'expires_hours': 24,
        }

        subject = 'Analizus - E-posta Adresinizi Doğrulayın'

        # E-posta yapılandırılmamışsa skip et
        if not cls.is_configured():
            logger.warning(f"E-posta yapılandırılmamış. Kullanıcı: {user.username}")
            return False

        # HTML template
        html_message = render_to_string('forum/emails/verification_email.html', context)
        plain_message = strip_tags(html_message)

        try:
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                html_message=html_message,
                fail_silently=False,
            )
            logger.info(f"Doğrulama e-postası gönderildi: {user.email}")
            return True
        except Exception as e:
            logger.error(f"E-posta gönderme hatası ({user.email}): {e}")
            return False

    @classmethod
    def send_welcome_email(cls, user):
        """
        Doğrulama sonrası hoş geldin e-postası gönderir

        Args:
            user: User modeli instance

        Returns:
            bool: Gönderim başarılı mı
        """
        context = {
            'user': user,
            'site_url': cls.get_base_url(),
            'site_name': 'Analizus',
        }

        subject = 'Analizus\'a Hoş Geldiniz!'

        # E-posta yapılandırılmamışsa skip et
        if not cls.is_configured():
            logger.warning(f"E-posta yapılandırılmamış. Hoş geldin e-postası gönderilemedi: {user.username}")
            return False

        html_message = render_to_string('forum/emails/welcome_email.html', context)
        plain_message = strip_tags(html_message)

        try:
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                html_message=html_message,
                fail_silently=False,
            )
            logger.info(f"Hoş geldin e-postası gönderildi: {user.email}")
            return True
        except Exception as e:
            logger.error(f"E-posta gönderme hatası ({user.email}): {e}")
            return False

    @classmethod
    def send_resend_verification_email(cls, user, verification_token):
        """
        Tekrar doğrulama e-postası gönderir (kullanıcı talep ettiğinde)

        Args:
            user: User modeli instance
            verification_token: EmailVerification modeli instance

        Returns:
            bool: Gönderim başarılı mı
        """
        # Aynı verification_email fonksiyonunu kullanabiliriz
        return cls.send_verification_email(user, verification_token)
