import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """
        Kullanıcı WebSocket'e bağlandığında çağrılır.
        Kullanıcıyı doğrular ve ona özel bir gruba ekler.
        """
        self.user = self.scope['user']
        
        if not self.user.is_authenticated:
            await self.close()
            return

        await self.accept()
        self.user_group_name = f'notifications_{self.user.id}'
        await self.channel_layer.group_add(
            self.user_group_name,
            self.channel_name
        )
        print(f"--- DEBUG: Kullanıcı '{self.user.username}' bağlandı ve '{self.user_group_name}' grubuna eklendi. ---") # HATA AYIKLAMA

    async def disconnect(self, close_code):
        """
        Kullanıcının bağlantısı kesildiğinde çağrılır.
        Kullanıcıyı grubundan çıkarır.
        """
        if self.user.is_authenticated:
            await self.channel_layer.group_discard(
                self.user_group_name,
                self.channel_name
            )

    async def notification_message(self, event):
        """
        Gruptan bir bildirim mesajı aldığında bu metot çağrılır.
        Mesajı WebSocket üzerinden client'a (kullanıcının tarayıcısına) gönderir.
        """
        print(f"--- DEBUG: '{self.user_group_name}' grubundaki consumer mesaj aldı. Tarayıcıya gönderiliyor... ---")
        message = event['message']
        url = event.get('url', '#')

        await self.send(text_data=json.dumps({
            'message': message,
            'url': url
        }))
