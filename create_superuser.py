import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "analizdestek.settings")
django.setup()

from django.contrib.auth.models import User

username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')

try:
    if not User.objects.filter(username=username).exists():
        # Kullanıcı yoksa oluştur
        print(f"🛠️ Kullanıcı oluşturuluyor: {username}")
        User.objects.create_superuser(username, email, password)
        print("✅ Süper kullanıcı oluşturuldu!")
    else:
        # Kullanıcı varsa ŞİFRESİNİ ZORLA GÜNCELLE
        print(f"🔄 Kullanıcı zaten var. Şifre güncelleniyor: {username}")
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        print("✅ Şifre başarıyla güncellendi!")

except Exception as e:
    print(f"❌ Hata oluştu: {e}")