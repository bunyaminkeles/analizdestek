from django.contrib import admin
from django.utils.html import format_html
from .models import Section, Category, Topic, Post, Profile, ContactMessage

# --- GENEL AYARLAR ---
admin.site.site_header = "AnalizDestek Komuta Merkezi"
admin.site.site_title = "Vizyon 2050 Admin"
admin.site.index_title = "Sistem Yönetim Paneli"

# 1. Kategori Yönetimi (Inline)
class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1
    prepopulated_fields = {'slug': ('title',)}
    classes = ['collapse']

# 2. Ana Bölüm (Section) Yönetimi
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    # DÜZELTME: 'order' düzenlenebilir olduğu için listede de görünmek ZORUNDA
    list_display = ('title', 'order', 'order_visual', 'category_count') 
    list_editable = ('order',)
    inlines = [CategoryInline]
    ordering = ('order',)

    def order_visual(self, obj):
        return format_html(
            '<div style="width:{}px; background:#00d2ff; height:10px; border-radius:5px;"></div>',
            obj.order * 10
        )
    order_visual.short_description = "Görsel Öncelik"

    def category_count(self, obj):
        return obj.categories.count()
    category_count.short_description = "Kategori Sayısı"

# 3. Konu (Topic) Yönetimi
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    # Modeller güncellendiği için artık hata vermez
    list_display = ('subject_link', 'category_colored', 'starter', 'created_at', 'views', 'status_icons')
    list_filter = ('is_pinned', 'is_closed', 'category', 'created_at') 
    search_fields = ('subject', 'starter__username')
    date_hierarchy = 'created_at'
    list_per_page = 20
    actions = ['make_pinned', 'make_unpinned', 'close_topic']

    def subject_link(self, obj):
        return format_html('<b>{}</b>', obj.subject)
    subject_link.short_description = "Konu Başlığı"

    def category_colored(self, obj):
        return format_html(
            '<span style="color: #00d2ff; font-weight:bold;">{}</span>', 
            obj.category.title
        )
    category_colored.short_description = "Kategori"

    def status_icons(self, obj):
        icons = []
        if obj.is_pinned:
            icons.append('<i class="fas fa-thumbtack" style="color:#ffc107; margin-right:5px;" title="Sabit"></i>')
        if obj.is_closed:
            icons.append('<i class="fas fa-lock" style="color:#dc3545;" title="Kilitli"></i>')
        if not icons:
            return "-"
        return format_html(" ".join(icons))
    status_icons.short_description = "Durum"

    @admin.action(description='Seçilenleri SABİTLE')
    def make_pinned(self, request, queryset):
        queryset.update(is_pinned=True)

    @admin.action(description='Seçilenlerin sabitini KALDIR')
    def make_unpinned(self, request, queryset):
        queryset.update(is_pinned=False)
        
    @admin.action(description='Seçilen konuları KİLİTLE')
    def close_topic(self, request, queryset):
        queryset.update(is_closed=True)

# 4. Mesaj (Post) Yönetimi
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author_link', 'topic_link', 'short_message_preview', 'created_at')
    search_fields = ('message', 'author__username')
    list_filter = ('created_at',)
    autocomplete_fields = ['topic', 'author']

    def short_message_preview(self, obj):
        return obj.message[:60] + '...' if len(obj.message) > 60 else obj.message
    short_message_preview.short_description = "İçerik Özeti"

    def topic_link(self, obj):
        return format_html('<a href="/admin/forum/topic/{}/change/">{}</a>', obj.topic.id, obj.topic.subject)
    topic_link.short_description = "Bağlı Olduğu Konu"

    def author_link(self, obj):
        return format_html('<span style="color:#a78bfa;">{}</span>', obj.author.username)
    author_link.short_description = "Yazar"

# 5. Profil Yönetimi
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # DÜZELTME: 'account_type' düzenlenebilir olduğu için listeye eklendi.
    # ARTIK 'location' alanı veritabanında olduğu için buraya da eklendi.
    list_display = ('avatar_preview', 'user_info', 'account_type', 'account_type_badge', 'location', 'title')
    list_filter = ('account_type', 'title')
    search_fields = ('user__username', 'bio', 'title', 'location')
    list_editable = ('account_type',) 
    list_per_page = 25

    def avatar_preview(self, obj):
        # Önce 'avatar' diye bir alan var mı ve dolu mu diye kontrol et
        if hasattr(obj, 'avatar') and obj.avatar:
            return format_html(
                '<img src="{}" style="width: 35px; height: 35px; border-radius: 50%; border: 2px solid #00d2ff;" />',
                obj.avatar.url
            )
        # Yoksa varsayılan ikon göster
        return format_html('<i class="fas fa-user-circle" style="font-size: 35px; color: #ccc;"></i>')
    avatar_preview.short_description = "Avatar"
    
    def user_info(self, obj):
        return format_html(
            '<strong>{}</strong><br><small style="color:#666;">{}</small>', 
            obj.user.username, obj.user.email
        )
    user_info.short_description = "Kullanıcı Detayı"

    def account_type_badge(self, obj):
        colors = {
            'Standard': 'secondary',
            'Premium': 'warning',
            'Expert': 'info',
            'Admin': 'danger'
        }
        color = colors.get(obj.account_type, 'secondary')
        return format_html(
            '<span class="badge badge-{}">{}</span>', 
            color, obj.account_type
        )
    account_type_badge.short_description = "Rozet"

# 6. İletişim Mesajları
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_link', 'subject', 'created_at_formatted')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)

    def email_link(self, obj):
        return format_html(
            '<a href="mailto:{}" class="btn btn-outline-primary btn-sm"><i class="fas fa-envelope"></i> {}</a>',
            obj.email, obj.email
        )
    email_link.short_description = "E-Posta (Yanıtla)"

    def created_at_formatted(self, obj):
        return obj.created_at.strftime("%d %b %Y, %H:%M")
    created_at_formatted.short_description = "Tarih"