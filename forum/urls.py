from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    
    # Profil
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),
    
    # Mesajlaşma
    path('inbox/', views.inbox, name='inbox'),
    path('send-message/<str:username>/', views.send_message, name='send_message'),  # ✅ YENİ

    # Forum
    path('forum/<slug:slug>/', views.category_topics, name='category_topics'),
    path('forum/<slug:slug>/new/', views.new_topic, name='new_topic'),
    path('topic/<int:pk>/', views.topic_detail, name='topic_detail'),
    path('topic/<int:pk>/summarize/', views.summarize_topic, name='summarize_topic'),
    
    # Diğer
    path('search/', views.search_result, name='search'),
    path('hakkimizda/', views.about, name='about'),
    path('iletisim/', views.contact, name='contact'),
    
    # Section Detail
    path('section/<int:pk>/', views.section_detail, name='section_detail'),
]