from django.contrib import admin
from django.utils.html import format_html
from .models import Section, Category, Topic, Post, Profile, ContactMessage, PrivateMessage

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

# 6. Profil Yönetimi
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar_preview', 'account_type', 'title', 'location', 'email_preferences')
    list_editable = ('account_type',)
    search_fields = ('user__username', 'title')
    list_filter = ('account_type',)

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" style="width: 40px; height: 40px; border-radius: 50%; object-fit: cover;">', obj.avatar.url)
        return format_html('<div style="width: 40px; height: 40px; border-radius: 50%; background: #555; display: flex; align-items: center; justify-content: center; color: white;">{}</div>', obj.user.username[0].upper())
    avatar_preview.short_description = "Avatar"

    def account_type_colored(self, obj):
        colors = {'Free': '#6c757d', 'Premium': '#FFD700', 'Expert': '#00d2ff'}
        return format_html('<span style="color: {}; font-weight: bold;">{}</span>', colors.get(obj.account_type, '#fff'), obj.get_account_type_display())
    account_type_colored.short_description = "Üyelik Türü"

    def email_preferences(self, obj):
        icons = []
        if obj.email_on_reply:
            icons.append('<span title="Konuma cevap bildirimi açık">💬</span>')
        if obj.email_on_private_message:
            icons.append('<span title="Özel mesaj bildirimi açık">✉️</span>')
        return format_html(' '.join(icons) if icons else '<span style="color: #888;">Bildirim kapalı</span>')
    email_preferences.short_description = "Email Tercihleri"

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