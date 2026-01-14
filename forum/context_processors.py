from .models import PrivateMessage

def unread_messages_count(request):
    if request.user.is_authenticated:
        try:
            # Kullanıcının okunmamış mesaj sayısını çekiyoruz
            count = PrivateMessage.objects.filter(receiver=request.user, is_read=False).count()
            return {'unread_count': count}
        except:
            # Henüz tablo oluşmadıysa hata verme, 0 döndür
            return {'unread_count': 0}
    return {'unread_count': 0}