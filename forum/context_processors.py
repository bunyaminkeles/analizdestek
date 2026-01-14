from .models import PrivateMessage
from django.db import connection

def unread_messages_count(request):
    if request.user.is_authenticated:
        # Önce tablo veritabanında gerçekten var mı diye kontrol et (Zırh katmanı)
        table_name = PrivateMessage._meta.db_table
        if table_name in connection.introspection.table_names():
            try:
                count = PrivateMessage.objects.filter(receiver=request.user, is_read=False).count()
                return {'unread_count': count}
            except:
                return {'unread_count': 0}
    return {'unread_count': 0}