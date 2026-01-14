from .models import PrivateMessage
from django.db import connection

def unread_messages_count(request):
    data = {'unread_count': 0}
    if request.user.is_authenticated:
        try:
            # SİGORTA: Tablo veritabanında var mı kontrol et
            with connection.cursor() as cursor:
                table_names = connection.introspection.table_names(cursor)
                if PrivateMessage._meta.db_table in table_names:
                    count = PrivateMessage.objects.filter(receiver=request.user, is_read=False).count()
                    data['unread_count'] = count
        except Exception as e:
            # Hata ne olursa olsun siteyi çökertme
            print(f"DM Gözcü Hatası: {e}")
            pass
    return data