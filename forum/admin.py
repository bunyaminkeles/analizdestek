from django.contrib import admin
from .models import Section, Category, Topic, Post, Profile

# 1. Kategorileri, Ana Bölümlerin (Section) içinde yönetmek için 'Inline' yapısı
class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1
    prepopulated_fields = {'slug': ('title',)}

# 2. Section (Ana Bölüm) Yönetimi
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    inlines = [CategoryInline]

# 3. Topic (Konu) Yönetimi
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    # 'is_pinned' modelde olmadığı için listeden çıkardım
    list_display = ('subject', 'category', 'starter', 'created_at', 'views')
    list_filter = ('category', 'created_at')
    search_fields = ('subject', 'starter__username')
    date_hierarchy = 'created_at'

# 4. Post (Mesaj) Yönetimi
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'topic', 'short_message', 'created_at')
    search_fields = ('message', 'author__username')
    list_filter = ('created_at',)

    def short_message(self, obj):
        return obj.message[:75] + '...' if len(obj.message) > 75 else obj.message
    short_message.short_description = "Mesaj Özeti"

# 5. Profil ve Üyelik Yönetimi
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # Modelde 'university' ve 'reputation' olmadığı için onları kaldırdım
    list_display = ('user', 'title', 'account_type')
    list_filter = ('account_type', 'title') 
    search_fields = ('user__username', 'title')
    list_editable = ('account_type',)