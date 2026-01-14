from django.contrib import admin
from django.utils.html import format_html
from .models import Section, Category, Topic, Post, Profile, ContactMessage, PrivateMessage

# --- GENEL AYARLAR ---
admin.site.site_header = "AnalizDestek Komuta Merkezi"
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
        # Admin panelinde görsel bir bar oluşturur
        return format_html(
            '<div style="width:100px; background:#e9ecef; height:10px; border-radius:5px;">'
            '<div style="width:{}px; background:#00d2ff; height:10px; border-radius:5px;"></div>'
            '</div>',
            min(obj.order * 10, 100) # 100px ile sınırla
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

# 4. Mesaj (Post) Yönetimi
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'topic', 'short_message', 'created_at')
    search_fields = ('message', 'author__username')
    
    def short_message(self, obj):
        return obj.message[:50] + "..."

# 5. Özel Mesaj (DM) Yönetimi - YENİ EKLENDİ!
@admin.register(PrivateMessage)
class PrivateMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'short_content', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('sender__username', 'receiver__username', 'message')

    def short_content(self, obj):
        return obj.message[:50] + "..."
    short_content.short_description = "Mesaj İçeriği"

# 6. Profil Yönetimi
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_type', 'title', 'location')
    list_editable = ('account_type',)
    search_fields = ('user__username', 'title')

# 7. İletişim Mesajları
admin.site.register(ContactMessage)