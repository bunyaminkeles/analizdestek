# forum/routing.py
from django.urls import re_path

from .consumers import NotificationConsumer

# Gelen WebSocket bağlantılarını consumer'lara yönlendiren URL listesi
websocket_urlpatterns = [
    # 'ws://<alan_adi>/ws/notifications/' adresine gelen bağlantılar
    # NotificationConsumer tarafından yönetilecek.
    re_path(r'ws/notifications/$', NotificationConsumer.as_asgi()),
]
