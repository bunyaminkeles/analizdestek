from .models import PrivateMessage

def unread_messages_count(request):
    if request.user.is_authenticated:
        count = PrivateMessage.objects.filter(receiver=request.user, is_read=False).count()
        return {'unread_count': count}
    return {'unread_count': 0}