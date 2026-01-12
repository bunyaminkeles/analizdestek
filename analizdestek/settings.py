import os
from pathlib import Path
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# --- GÜVENLİK AYARLARI ---
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-varsayilan-anahtar')

# Yerelde True, Bulutta False olması için .env'den okuyoruz
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Bulut ortamında tüm domainlere izin ver (Gelişmiş güvenlik için ileride spesifikleştirilebilir)
ALLOWED_HOSTS = ['*']

# --- UYGULAMA TANIMLARI ---
INSTALLED_APPS = [
    'jazzmin',  # Admin paneli teması
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Kendi Uygulamalarımız
    'forum',
    'crispy_forms',
    'crispy_bootstrap5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # EN ÜSTTE OLMALI
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'analizdestek.urls'

# TEMPLATES (Tek bir blok olarak birleştirildi)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'analizdestek.wsgi.application'

# --- VERİTABANI ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- STATİK DOSYALAR (Cloud Uyumluluğu) ---
# STATIC ayarlarını dosyanın en sonunda kontrol et:
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / "staticfiles"

# Yerel geliştirme yaparken bunu geçici olarak yorum satırı yapabilirsin
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# --- DİĞER AYARLAR ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LANGUAGE_CODE = 'tr' # Türkçe dil desteği
TIME_ZONE = 'Europe/Istanbul' # Türkiye saat dilimi
USE_I18N = True
USE_TZ = True

# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Yönlendirmeler
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

# OpenAI API Key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Jazzmin Admin Ayarları (Kısaltıldı)
JAZZMIN_SETTINGS = {
    "site_title": "AnalizDestek Admin",
    "site_brand": "AnalizDestek AI",
    "theme": "flatly",
}