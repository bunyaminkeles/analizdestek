from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    def handle(self, *args, **options):
        username = "bunyamin"  # İstediğin kullanıcı adını yazabilirsin
        email = "admin@example.com"
        password = os.getenv("ADMIN_PASSWORD", "Admin123!") # Şifreyi Render'dan alacak

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f'Admin kullanıcısı "{username}" başarıyla oluşturuldu.'))
        else:
            self.stdout.write(self.style.WARNING(f'Admin kullanıcısı "{username}" zaten mevcut.'))