from django.contrib import admin
from django.utils.html import format_html
from .models import Section, Category, Topic, Post, Profile, ContactMessage, PrivateMessage, Badge, Notification, Skill

# --- GENEL AYARLAR ---
admin.site.site_header = "Analizus Komuta Merkezi"
admin.site.site_title = "Vizyon 2050 Admin"
admin.site.index_title = "Sistem Yönetim Paneli"

# 1. Kategori Yönetimi (Inline)
class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1
    prepopulated_fields = {'slug': ('title',)}

# 2. Ana Bölüm (Section) Yönetimi
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'order_visual', 'category_count') 
    list_editable = ('order',)
    inlines = [CategoryInline]
    ordering = ('order',)

    def order_visual(self, obj):
        return format_html(
            '<div style="width:100px; background:#e9ecef; height:10px; border-radius:5px;">'
            '<div style="width:{}px; background:#00d2ff; height:10px; border-radius:5px;"></div>'
            '</div>',
            min(obj.order * 10, 100)
        )
    order_visual.short_description = "Görsel Sıralama"

    def category_count(self, obj):
        return obj.categories.count()
    category_count.short_description = "Kategori Sayısı"

# 3. Konu (Topic) Yönetimi
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('subject_link', 'category_colored', 'starter', 'created_at', 'views', 'status')
    list_filter = ('is_pinned', 'is_closed', 'category', 'created_at')
    search_fields = ('subject', 'starter__username')
    date_hierarchy = 'created_at'
    actions = ['make_pinned', 'make_unpinned', 'make_closed', 'make_open']

    def subject_link(self, obj):
        return format_html('<b>{}</b>', obj.subject)
    subject_link.short_description = "Konu Başlığı"

    def category_colored(self, obj):
        return format_html('<span style="color: #00d2ff;">{}</span>', obj.category.title)

    def status(self, obj):
        res = []
        if obj.is_pinned: res.append("📌 Sabit")
        if obj.is_closed: res.append("🔒 Kilitli")
        return " | ".join(res) if res else "Normal"

    # Custom Actions
    @admin.action(description='📌 Seçili konuları sabitle')
    def make_pinned(self, request, queryset):
        updated = queryset.update(is_pinned=True)
        self.message_user(request, f'{updated} konu sabitlendi.')

    @admin.action(description='📌 Sabitlemeyi kaldır')
    def make_unpinned(self, request, queryset):
        updated = queryset.update(is_pinned=False)
        self.message_user(request, f'{updated} konunun sabitlemesi kaldırıldı.')

    @admin.action(description='🔒 Seçili konuları kilitle')
    def make_closed(self, request, queryset):
        updated = queryset.update(is_closed=True)
        self.message_user(request, f'{updated} konu kilitlendi.')

    @admin.action(description='🔓 Seçili konuları aç')
    def make_open(self, request, queryset):
        updated = queryset.update(is_closed=False)
        self.message_user(request, f'{updated} konu açıldı.')

# 4. Mesaj (Post) Yönetimi - ✅ DÜZELTİLDİ
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'topic_link', 'short_message', 'created_at')
    search_fields = ('message', 'created_by__username', 'topic__subject')
    list_filter = ('created_at', 'topic__category')
    date_hierarchy = 'created_at'

    def short_message(self, obj):
        return obj.message[:50] + "..."
    short_message.short_description = "Mesaj"

    def topic_link(self, obj):
        return format_html('<a href="/admin/forum/topic/{}/change/" style="color: #00d2ff;">{}</a>', obj.topic.id, obj.topic.subject[:40])
    topic_link.short_description = "Konu"

# 5. Özel Mesaj (DM) Yönetimi
@admin.register(PrivateMessage)
class PrivateMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'short_content', 'created_at', 'read_status')
    list_filter = ('is_read', 'created_at')
    search_fields = ('sender__username', 'receiver__username', 'message')
    actions = ['mark_as_read', 'mark_as_unread']

    def short_content(self, obj):
        return obj.message[:50] + "..."
    short_content.short_description = "Mesaj İçeriği"

    def read_status(self, obj):
        if obj.is_read:
            return format_html('<span style="color: #28a745;">✅ Okundu</span>')
        return format_html('<span style="color: #dc3545; font-weight: bold;">❌ Okunmadı</span>')
    read_status.short_description = "Durum"

    # Custom Actions
    @admin.action(description='✅ Okundu olarak işaretle')
    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f'{updated} mesaj okundu olarak işaretlendi.')

    @admin.action(description='❌ Okunmadı olarak işaretle')
    def mark_as_unread(self, request, queryset):
        updated = queryset.update(is_read=False)
        self.message_user(request, f'{updated} mesaj okunmadı olarak işaretlendi.')

# 6. Yetenek (Skill) Yönetimi
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_preview', 'name', 'category', 'user_count')
    list_filter = ('category',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    def skill_preview(self, obj):
        return format_html(
            '<span style="background: {}; color: white; padding: 4px 10px; border-radius: 12px; font-size: 12px;">'
            '<i class="{}"></i> {}</span>',
            obj.color, obj.icon, obj.name
        )
    skill_preview.short_description = "Yetenek"

    def user_count(self, obj):
        return obj.users.count()
    user_count.short_description = "Kullanıcı Sayısı"


# 7. Rozet (Badge) Yönetimi
@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ('badge_preview', 'name', 'badge_type', 'points_required', 'user_count', 'is_active')
    list_filter = ('badge_type', 'is_active')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_active', 'points_required')

    def badge_preview(self, obj):
        return format_html(
            '<span style="background: {}; color: white; padding: 4px 10px; border-radius: 12px; font-size: 12px;">'
            '<i class="{}"></i> {}</span>',
            obj.color, obj.icon, obj.name
        )
    badge_preview.short_description = "Rozet"

    def user_count(self, obj):
        return obj.users.count()
    user_count.short_description = "Kullanıcı Sayısı"


# 8. Profil Yönetimi
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar_preview', 'rank_display', 'reputation', 'account_type', 'university_info', 'stats_display')
    list_editable = ('account_type',)
    search_fields = ('user__username', 'title', 'university', 'department')
    list_filter = ('account_type', 'rank', 'is_public')
    filter_horizontal = ('badges', 'skills')
    actions = ['update_all_ranks', 'update_all_stats']

    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('user', 'avatar', 'cover_image', 'bio', 'title', 'location')
        }),
        ('Akademik Bilgiler', {
            'fields': ('university', 'department', 'academic_title'),
            'classes': ('collapse',)
        }),
        ('Sosyal Medya', {
            'fields': ('website', 'linkedin', 'twitter', 'github', 'orcid', 'google_scholar'),
            'classes': ('collapse',)
        }),
        ('Sistem Bilgileri', {
            'fields': ('account_type', 'rank', 'reputation', 'badges', 'skills')
        }),
        ('İstatistikler', {
            'fields': ('total_topics', 'total_posts', 'total_likes_received', 'best_answers_count'),
            'classes': ('collapse',)
        }),
        ('Tercihler', {
            'fields': ('email_on_reply', 'email_on_private_message', 'is_public', 'show_email'),
            'classes': ('collapse',)
        }),
    )

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" style="width: 40px; height: 40px; border-radius: 50%; object-fit: cover;">', obj.avatar.url)
        return format_html('<div style="width: 40px; height: 40px; border-radius: 50%; background: #555; display: flex; align-items: center; justify-content: center; color: white;">{}</div>', obj.user.username[0].upper())
    avatar_preview.short_description = "Avatar"

    def rank_display(self, obj):
        rank_info = obj.get_rank_display_with_icon()
        return format_html(
            '<span style="color: {};">{} {}</span>',
            rank_info['color'], rank_info['icon'], rank_info['name']
        )
    rank_display.short_description = "Rütbe"

    def university_info(self, obj):
        if obj.university:
            return format_html('<span title="{}">{}</span>', obj.department or '-', obj.university[:20] + '...' if len(obj.university) > 20 else obj.university)
        return format_html('<span style="color: #888;">-</span>')
    university_info.short_description = "Üniversite"

    def stats_display(self, obj):
        return format_html(
            '<span title="Konu: {}, Gönderi: {}, Beğeni: {}">📊 {}/{}/{}</span>',
            obj.total_topics, obj.total_posts, obj.total_likes_received,
            obj.total_topics, obj.total_posts, obj.total_likes_received
        )
    stats_display.short_description = "İstatistikler"

    @admin.action(description='🔄 Seçili kullanıcıların rütbelerini güncelle')
    def update_all_ranks(self, request, queryset):
        for profile in queryset:
            profile.update_rank()
        self.message_user(request, f'{queryset.count()} kullanıcının rütbesi güncellendi.')

    @admin.action(description='📊 Seçili kullanıcıların istatistiklerini güncelle')
    def update_all_stats(self, request, queryset):
        for profile in queryset:
            profile.update_stats()
        self.message_user(request, f'{queryset.count()} kullanıcının istatistikleri güncellendi.')


# 8. Bildirim Yönetimi
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'sender', 'verb', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('recipient__username', 'sender__username', 'verb')
    date_hierarchy = 'created_at'
    actions = ['mark_as_read']

    @admin.action(description='✅ Okundu olarak işaretle')
    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f'{updated} bildirim okundu olarak işaretlendi.')

# 7. İletişim Mesajları
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at_formatted', 'preview_message')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

    def created_at_formatted(self, obj):
        return format_html('<span style="color: #00d2ff;">{}</span>', obj.created_at.strftime('%d %b %Y, %H:%M'))
    created_at_formatted.short_description = "Tarih"

    def preview_message(self, obj):
        return obj.message[:100] + "..." if len(obj.message) > 100 else obj.message
    preview_message.short_description = "Mesaj Önizleme"