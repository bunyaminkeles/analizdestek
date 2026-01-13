from django.urls import path, include
from . import views

urlpatterns = [
    # Ana Sayfa
    path('', views.home, name='home'),
    
    # Üyelik İşlemleri
    path('register/', views.register, name='register'),

    # Profil İşlemleri (SIRALAMA KRİTİK!)
    # Önce sabit/özel yollar (edit), sonra değişken yollar (username) gelmeli
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),

    # Forum İşlemleri
    path('forum/<slug:slug>/', views.category_topics, name='category_topics'),
    path('forum/<slug:slug>/new/', views.new_topic, name='new_topic'),
    
    # Konu Detay ve Özetleme
    path('topic/<int:pk>/', views.topic_detail, name='topic_detail'),
    path('topic/<int:pk>/summarize/', views.summarize_topic, name='summarize_topic'),
    
    # Arama ve Diğer Sayfalar
    path('search/', views.search_result, name='search'),
    path('hakkimizda/', views.about, name='about'),
    path('iletisim/', views.contact, name='contact'),
    path('i18n/', include('django.conf.urls.i18n')),
]