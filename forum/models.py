from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

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

    def get_absolute_url(self):
        return reverse('topic_detail', kwargs={'pk': self.pk})

    @property
    def last_post(self):
        """Bu konuya atılan son gönderiyi döndürür."""
        return self.posts.order_by('-created_at').first()

class Post(models.Model):
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    message = models.TextField()
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_best_answer = models.BooleanField(default=False, verbose_name="En Faydalı Yanıt")
    likes = models.PositiveIntegerField(default=0, verbose_name="Beğeni Sayısı")

    def __str__(self):
        return f"Post by {self.created_by.username}"

    def get_absolute_url(self):
        topic_url = self.topic.get_absolute_url()
        return f"{topic_url}#post-{self.id}"

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
    reputation = models.IntegerField(default=0, verbose_name="Akademik Puan")
    
    # ✅ EMAIL BİLDİRİM TERCİHLERİ
    email_on_reply = models.BooleanField(default=True, verbose_name="Konuma cevap geldiğinde email gönder")
    email_on_private_message = models.BooleanField(default=True, verbose_name="Özel mesaj geldiğinde email gönder")
    
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


class PostLike(models.Model):
    """Kullanıcıların post beğenilerini takip eden model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')  # Her kullanıcı bir post'a sadece 1 kez like verebilir
        verbose_name = "Beğeni"
        verbose_name_plural = "Beğeniler"

    def __str__(self):
        return f"{self.user.username} liked Post #{self.post.id}"

class Notification(models.Model):
    """Gerçek zamanlı bildirimler için model"""
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications', verbose_name="Alıcı")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications', null=True, blank=True, verbose_name="Gönderen")
    verb = models.CharField(max_length=255, verbose_name="Eylem")
    
    # Bildirimin ilişkili olduğu nesne (örneğin, bir Post, bir Topic, vb.)
    # ContentType framework'ü kullanılarak esnek bir yapı oluşturulur.
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    target = GenericForeignKey('content_type', 'object_id')

    is_read = models.BooleanField(default=False, verbose_name="Okundu mu?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Zamanı")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Bildirim"
        verbose_name_plural = "Bildirimler"

    def __str__(self):
        if self.target:
            return f"{self.sender.username} -> {self.recipient.username}: {self.verb} -> {self.target}"
        return f"{self.sender.username} -> {self.recipient.username}: {self.verb}"
