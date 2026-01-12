from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    # Ana Sayfa
    path('', views.home, name='home'),
    
    # Üyelik İşlemleri
    path('register/', views.register, name='register'),

    # Forum İşlemleri
    path('forum/<slug:slug>/', views.category_topics, name='category_topics'),
    
    # YENİ KONU AÇMA (Sıralama Önemli: Slug'dan sonra gelebilir ama çakışmaz)
    path('forum/<slug:slug>/new/', views.new_topic, name='new_topic'),
    
    # Konu Detay ve Özetleme
    path('topic/<int:pk>/', views.topic_detail, name='topic_detail'),
    path('topic/<int:pk>/summarize/', views.summarize_topic, name='summarize_topic'),
    
    # Profil ve Arama
    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),
    path('search/', views.search_result, name='search_result'),
    path('hakkimizda/', views.about, name='about'), # EKLENEN
    path('iletisim/', views.contact, name='contact'), # EKLENEN
    path('i18n/', include('django.conf.urls.i18n')), # Dil değiştirme rotası
]