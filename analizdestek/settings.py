import os
import dj_database_url # <-- BU SATIR EKLENDİ
from pathlib import Path
from dotenv import load_dotenv
from django.utils.translation import gettext_lazy as _



# .env dosyasını yükle
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# --- GÜVENLİK AYARLARI ---
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-varsayilan-anahtar')

# Canlıda Debug KAPALI olmalı, yoksa hacklenirsin.
# Ancak şimdilik os.environ.get ile kontrol ediyoruz.
DEBUG = 'RENDER' not in os.environ

# Sunucu adresini kabul et
ALLOWED_HOSTS = ['*'] # Yıldız (*) koyarsan her yerden açılır (Render URL'i dahil)

# Alan Adı ve Güvenlik
# ALLOWED_HOSTS = ['analizdestek-ai.onrender.com', '127.0.0.1', 'localhost']
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
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', # 1. Önce Oturum
    'django.middleware.common.CommonMiddleware',             # 2. Sonra Common
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',            # 3. DİL BURADA OLMALI!
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
            ],
        },
    },
]

WSGI_APPLICATION = 'analizdestek.wsgi.application'

# --- VERİTABANI (Render PostgreSQL / Local SQLite) ---
# settings.py
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'),
        conn_max_age=600
    )
}

# --- STATİK DOSYALAR ---
STATIC_URL = '/static/'
# Bu klasör canlıda dosyaların toplanacağı yer
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Whitenoise sıkıştırma ayarı (Hız için)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Senin oluşturduğun static klasörleri
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

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

AZZMIN_SETTINGS = {
    # Başlıklar ve Logolar
    "site_title": "AnalizDestek Komuta Merkezi",
    "site_header": "Vizyon 2050",
    "site_brand": "AnalizDestek Yöneticisi",
    "welcome_sign": "Komuta Merkezine Hoş Geldiniz, Sayın CEO",
    "copyright": "AnalizDestek Ltd.",
    "search_model": ["auth.User", "forum.Topic"], # CTRL+K ile her şeyi buradan arayacaksın!

    # Menü Ayarları
    "topmenu_links": [
        {"name": "Ana Siteye Dön", "url": "home", "permissions": ["auth.view_user"]},
        {"name": "Destek Hattı", "url": "https://wa.me/905xxxxxx", "new_window": True},
        {"model": "auth.User"}, # Kullanıcılara hızlı erişim
    ],

    # Kullanıcı Menüsü
    "usermenu_links": [
        {"name": "Profilim", "url": "profile_detail", "new_window": False},
        {"model": "auth.user"}
    ],

    # Yan Menü (Sidebar) Düzeni
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],

    # İkonlar (Bootstrap Icons kullanır)
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "forum.Topic": "fas fa-comments",       # Konular için ikon
        "forum.Category": "fas fa-layer-group", # Kategoriler için ikon
        "forum.Post": "fas fa-comment-dots",    # Mesajlar için ikon
    },
    
    # Özel CSS/JS eklemek istersen
    "custom_css": None,
    "custom_js": None,
    
    # TASARIM AYARLARI (KRİTİK)
    "show_ui_builder": True, # Canlı tema düzenleyiciyi açar (İşin bitince False yap)
}

# CEO'YA YAKIŞIR KARANLIK TEMA AYARLARI
JAZZMIN_UI_TWEAKS = {
    "custom_css": "css/admin_theme.css",
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    "accent": "accent-info",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-info", # Yan menü karanlık ve neon mavi detaylı
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "cyborg", # İŞTE BU! "Cyborg" teması tam senin sitene göre (Simsiyah ve Neon)
    "dark_mode_theme": "cyborg",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}


# --- ADMIN KURTARMA OPERASYONU ---
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth import get_user_model

@receiver(post_migrate)
def create_superuser_after_migrate(sender, **kwargs):
    User = get_user_model()
    if not User.objects.filter(username='teğmen').exists():
        User.objects.create_superuser('teğmen', 'admin@example.com', 'Vizyon2050!')
        print("🚀 CEO Hesabı (teğmen) Sızma Başarılı!")