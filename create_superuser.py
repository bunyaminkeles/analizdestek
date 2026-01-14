import os
import django
from django.contrib.auth.models import User

# Django ayarlarını yükle
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "analizdestek.settings")
django.setup()



# Bilgileri Render ayarlarından alacağız
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'bunyamin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'bkeles74@gmail.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'Yakup1992-') # Güvenlik için değiştireceğiz

if not User.objects.filter(username=username).exists():
    print(f"Süper kullanıcı oluşturuluyor: {username}")
    User.objects.create_superuser(username, email, password)
    print("Süper kullanıcı başarıyla oluşturuldu! 🚀")
else:
    print("Süper kullanıcı zaten var. Atlanıyor. 😎")