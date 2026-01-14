from .models import PrivateMessage

def unread_messages_count(request):
    """Giriş yapmış kullanıcılar için okunmamış mesaj sayısını döndürür."""
    if request.user.is_authenticated:
        try:
            count = PrivateMessage.objects.filter(receiver=request.user, is_read=False).count()
            return {'unread_count': count}
        except Exception:
            return {'unread_count': 0}
    return {'unread_count': 0}