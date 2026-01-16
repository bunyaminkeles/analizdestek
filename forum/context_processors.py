from django.conf import settings


def unread_messages_count(request):
    return {'unread_count': 0}


def google_analytics(request):
    """Google Analytics ID'yi tüm template'lere geçirir"""
    return {'GOOGLE_ANALYTICS_ID': getattr(settings, 'GOOGLE_ANALYTICS_ID', '')}