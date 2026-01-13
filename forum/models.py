from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Section(models.Model):
    """Ana Bölümler: Örn: Nicel Analizler"""
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0, verbose_name="Sıralama")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Category(models.Model):
    """Alt Forumlar: Örn: SPSS Destek"""
    # DİKKAT: related_name='categories' BURADA KRİTİK
    section = models.ForeignKey(Section, related_name='categories', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.CharField(max_length=255, blank=True)
    icon_class = models.CharField(max_length=50, default="bi-chat-square-text")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title.replace('ı', 'i'))
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Topic(models.Model):
    """Konu Başlıkları"""
    # DİKKAT: related_name='topics' BURADA KRİTİK (Yoksa '0 Konu' yazar veya hata verir)
    category = models.ForeignKey(Category, related_name='topics', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255, verbose_name="Konu Başlığı")
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.subject

class Post(models.Model):
    """Mesajlar"""
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    message = models.TextField(verbose_name="Mesaj")
    created_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    """Kullanıcı Profili"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20, default='Standard') # Standard, Premium, Expert
    title = models.CharField(max_length=100, blank=True, null=True) # Örn: Veri Bilimci

    def __str__(self):
        return self.user.username
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"