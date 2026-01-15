from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Section(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Category(models.Model):
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
    category = models.ForeignKey(Category, related_name='topics', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    # ✅ EKSİK ALANLAR EKLENDİ
    is_pinned = models.BooleanField(default=False, verbose_name="Sabitlenmiş")
    is_closed = models.BooleanField(default=False, verbose_name="Kilitli")

    def __str__(self):
        return self.subject

class Post(models.Model):
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    message = models.TextField()
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.created_by.username}"

class Profile(models.Model):
    ACCOUNT_TYPES = (
        ('Free', 'Ücretsiz Üye'),
        ('Premium', 'Premium Üye'),
        ('Expert', 'Uzman'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    # ✅ EKSİK ALANLAR EKLENDİ (Varsayılan değerlerle)
    title = models.CharField(max_length=100, blank=True, default="", verbose_name="Ünvan")
    location = models.CharField(max_length=100, blank=True, default="", verbose_name="Konum")
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES, default='Free')
    
    def __str__(self):
        return self.user.username

class PrivateMessage(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"