from .models import PrivateMessage

def unread_messages_count(request):
    # Varsayılan olarak 0 döndür
    data = {'unread_count': 0}
    
    if request.user.is_authenticated:
        try:
            # Sadece alıcısı kullanıcı olan ve okunmamış mesajları say
            count = PrivateMessage.objects.filter(receiver=request.user, is_read=False).count()
            data['unread_count'] = count
        except Exception as e:
            # Veritabanı hatası olsa bile siteyi çökertme, loga yaz
            print(f"Context Processor Hatası: {e}")
            pass
            
    return data