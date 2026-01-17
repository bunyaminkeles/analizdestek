"""
E-posta gönderme servisi
"""
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.urls import reverse


class EmailService:
    """E-posta gönderme işlemlerini yöneten servis"""

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
            return True
        except Exception as e:
            print(f"E-posta gönderme hatası: {e}")
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
            return True
        except Exception as e:
            print(f"E-posta gönderme hatası: {e}")
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
