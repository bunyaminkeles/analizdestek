import os
import dj_database_url # <-- BU SATIR EKLENDİ
from pathlib import Path
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# --- GÜVENLİK AYARLARI ---
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-varsayilan-anahtar')

# Yerelde True, Bulutta False
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Alan Adı ve Güvenlik
ALLOWED_HOSTS = ['analizdestek-ai.onrender.com', '127.0.0.1', 'localhost']
CSRF_TRUSTED_ORIGINS = ['https://analizdestek-ai.onrender.com']

# --- UYGULAMA TANIMLARI ---
INSTALLED_APPS = [
    'jazzmin',  # Admin paneli teması (En üstte kalmalı)
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
    'whitenoise.middleware.WhiteNoiseMiddleware', # Statik dosyalar için
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'analizdestek.urls'

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

# --- VERİTABANI (Render PostgreSQL / Local SQLite) ---
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600
    )
}

# --- STATİK DOSYALAR ---
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / "staticfiles"

if not DEBUG:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    # Canlı ortamda HTTPS zorunluluğu
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# --- DİĞER AYARLAR ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LANGUAGE_CODE = 'tr'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_TZ = True

# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Yönlendirmeler
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

# API Anahtarları
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# --- JAZZMIN AYARLARI (GÜNCELLENDİ) ---
JAZZMIN_SETTINGS = {
    "site_title": "AnalizDestek Admin",
    "site_header": "AnalizDestek",
    "site_brand": "AnalizDestek AI",
    "welcome_sign": "Akademik Veri Üssü Yönetim Paneli",
    "copyright": "AnalizDestek v2.0",
    "search_model": ["auth.User", "forum.Topic"],
    "theme": "darkly", # 2050 vizyonu için koyu tema
    "dark_mode_theme": "darkly",
}

# Güvenlik Headerları
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'