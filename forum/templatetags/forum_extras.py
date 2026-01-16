from django import template

register = template.Library()

@register.filter
def get_user_rank(user):
    """
    Kullanıcının mesaj sayısına göre rütbesini ve CSS rengini belirler.
    Döndüreceği format: (Rütbe Adı, CSS Class'ı, İkon)
    """
    if not user.is_authenticated:
        return "Ziyaretçi", "secondary", "bi-person"
    
    # Rütbeyi artık Akademik Puan (Reputation) belirliyor
    reputation = user.profile.reputation if hasattr(user, 'profile') else 0
    
    if user.is_superuser:
        return "Sistem Yöneticisi", "danger", "bi-shield-lock-fill" # Kırmızı

    if reputation < 50:
        return "Veri Çırağı", "secondary", "bi-battery" # Gri
    elif reputation < 200:
        return "Kod Gezgini", "info", "bi-battery-half" # Mavi
    elif reputation < 500:
        return "Algoritma Mimarı", "success", "bi-battery-charging" # Yeşil
    elif reputation < 1000:
        return "Veri Bilimci", "warning", "bi-cpu-fill" # Turuncu
    else:
        return "CYBER ORACLE", "primary", "bi-stars" # Neon Mavi/Parlak