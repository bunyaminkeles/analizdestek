from django import template
from django.utils.safestring import mark_safe

register = template.Library()


# Rütbe bilgileri: (rütbe_key): (isim, renk, ikon, css_class)
RANK_INFO = {
    'newbie': ('Çaylak', '#94a3b8', '🌱', 'secondary'),
    'member': ('Üye', '#64748b', '👤', 'secondary'),
    'active': ('Aktif Üye', '#3b82f6', '⚡', 'info'),
    'contributor': ('Katkıcı', '#8b5cf6', '✍️', 'primary'),
    'expert': ('Uzman', '#f59e0b', '🎯', 'warning'),
    'master': ('Usta', '#ef4444', '👑', 'danger'),
    'legend': ('Efsane', '#eab308', '🏆', 'warning'),
    'admin': ('Yönetici', '#dc2626', '🛡️', 'danger'),
}


@register.filter
def get_user_rank(user):
    """
    Kullanıcının rütbesini ve CSS bilgilerini döndürür.
    Döndüreceği format: (Rütbe Adı, CSS Class'ı, İkon)
    """
    if not user.is_authenticated:
        return "Ziyaretçi", "secondary", "bi-person"

    if not hasattr(user, 'profile'):
        return "Çaylak", "secondary", "🌱"

    rank = user.profile.rank
    info = RANK_INFO.get(rank, RANK_INFO['newbie'])
    return info[0], info[3], info[2]


@register.filter
def get_rank_badge(user):
    """Kullanıcının rütbe badge'ini HTML olarak döndürür"""
    if not user.is_authenticated:
        return mark_safe('<span class="badge bg-secondary">Ziyaretçi</span>')

    if not hasattr(user, 'profile'):
        return mark_safe('<span class="badge bg-secondary">🌱 Çaylak</span>')

    rank = user.profile.rank
    info = RANK_INFO.get(rank, RANK_INFO['newbie'])
    name, color, icon, css = info

    return mark_safe(f'<span class="badge" style="background-color: {color};">{icon} {name}</span>')


@register.filter
def get_user_badges(user, limit=3):
    """Kullanıcının rozetlerini döndürür"""
    if not user.is_authenticated or not hasattr(user, 'profile'):
        return []
    return user.profile.badges.all()[:limit]


@register.simple_tag
def render_badge(badge):
    """Rozeti HTML olarak render eder"""
    return mark_safe(
        f'<span class="badge me-1" style="background-color: {badge.color};" '
        f'title="{badge.description}">'
        f'<i class="{badge.icon}"></i> {badge.name}</span>'
    )


@register.simple_tag
def render_user_badges(user, limit=3):
    """Kullanıcının rozetlerini HTML olarak render eder"""
    if not user.is_authenticated or not hasattr(user, 'profile'):
        return ''

    badges = user.profile.badges.all()[:limit]
    if not badges:
        return ''

    html_parts = []
    for badge in badges:
        html_parts.append(
            f'<span class="badge me-1" style="background-color: {badge.color}; font-size: 0.7rem;" '
            f'title="{badge.description}">'
            f'<i class="{badge.icon}"></i></span>'
        )

    extra_count = user.profile.badges.count() - limit
    if extra_count > 0:
        html_parts.append(f'<span class="text-muted small">+{extra_count}</span>')

    return mark_safe(''.join(html_parts))


@register.filter
def reputation_display(user):
    """Kullanıcının puanını formatlı gösterir"""
    if not user.is_authenticated or not hasattr(user, 'profile'):
        return "0"

    rep = user.profile.reputation
    if rep >= 1000:
        return f"{rep / 1000:.1f}K"
    return str(rep)