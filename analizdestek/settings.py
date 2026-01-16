import os
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv
from django.utils.translation import gettext_lazy as _

# .env dosyasını yükle
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# --- GÜVENLİK AYARLARI ---
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-varsayilan-anahtar')

# Canlıda Debug KAPALI olmalı.
DEBUG = 'RENDER' not in os.environ

# Sunucu adresini kabul et
ALLOWED_HOSTS = ['*']

# CSRF Güvenliği
CSRF_TRUSTED_ORIGINS = ['https://analizdestek-ai.onrender.com']

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
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
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
                'django.template.context_processors.i18n',
                'forum.context_processors.unread_messages_count', # BU GEÇİCİ OLARAK KAPALI
            ],
        },
    },
]

WSGI_APPLICATION = 'analizdestek.wsgi.application'

# --- VERİTABANI ---
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'),
        conn_max_age=600
    )
}

# --- STATİK DOSYALAR ---
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Canlı Ortam Güvenlik Ayarları
if not DEBUG:
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

# Güvenlik Headerları
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

LANGUAGES = [
    ('tr', _('Turkish')),
    ('en', _('English')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]

# --- ADMIN PANELİ AYARLARI (JAZZMIN) ---
JAZZMIN_SETTINGS = {  # DÜZELTME: AZZMIN -> JAZZMIN
    "site_title": "AnalizDestek Komuta Merkezi",
    "site_header": "Vizyon 2050",
    "site_brand": "AnalizDestek Yöneticisi",
    "welcome_sign": "Komuta Merkezine Hoş Geldiniz, Sayın CEO",
    "copyright": "AnalizDestek Ltd.",
    "search_model": ["auth.User", "forum.Topic"],

    "topmenu_links": [
        {"name": "Ana Siteye Dön", "url": "home", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
    ],

    "usermenu_links": [
        {"name": "Profilim", "url": "home", "new_window": False}, 
        {"model": "auth.user"}
    ],

    "show_sidebar": True,
    "navigation_expanded": True,
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "forum.Topic": "fas fa-comments",
        "forum.Category": "fas fa-layer-group",
        "forum.Post": "fas fa-comment-dots",
    },
    "show_ui_builder": True,
}

JAZZMIN_UI_TWEAKS = {
    "custom_css": "css/admin_theme.css",
    "theme": "cyborg",
    "dark_mode_theme": "cyborg",
    "navbar": "navbar-dark",
    "sidebar": "sidebar-dark-info",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}

# --- E-POSTA AYARLARI ---
# SendGrid kullanıyoruz (Render free tier SMTP desteklemiyor)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'  # SendGrid için sabit değer
EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_API_KEY', '')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'AnalizDestek <noreply@analizdestek-ai.onrender.com>')

# --- SESSION AYARLARI (Otomatik Logout) ---
SESSION_COOKIE_AGE = 60 * 60 * 24  # 24 saat (saniye cinsinden)
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Tarayıcı kapandığında oturum sonlanır
SESSION_SAVE_EVERY_REQUEST = True  # Her istekte session süresini yeniler (aktif kullanıcılar için)