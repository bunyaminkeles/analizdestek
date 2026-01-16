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

class Badge(models.Model):
    """Kullanıcılara verilebilecek rozetler/etiketler"""
    BADGE_TYPES = (
        ('achievement', 'Başarı'),
        ('specialty', 'Uzmanlık'),
        ('participation', 'Katılım'),
        ('special', 'Özel'),
    )

    name = models.CharField(max_length=50, verbose_name="Rozet Adı")
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=200, verbose_name="Açıklama")
    icon = models.CharField(max_length=50, default="bi-award", verbose_name="İkon (Bootstrap Icons)")
    color = models.CharField(max_length=20, default="#6366f1", verbose_name="Renk (Hex)")
    badge_type = models.CharField(max_length=20, choices=BADGE_TYPES, default='achievement')
    points_required = models.IntegerField(default=0, verbose_name="Gereken Puan (0=manuel)")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Rozet"
        verbose_name_plural = "Rozetler"
        ordering = ['-points_required']

    def __str__(self):
        return self.name


class Profile(models.Model):
    ACCOUNT_TYPES = (
        ('Free', 'Ücretsiz Üye'),
        ('Premium', 'Premium Üye'),
        ('Expert', 'Uzman'),
    )

    # Rütbe seviyeleri (puana göre otomatik atanır)
    RANK_CHOICES = (
        ('newbie', 'Çaylak'),
        ('member', 'Üye'),
        ('active', 'Aktif Üye'),
        ('contributor', 'Katkıcı'),
        ('expert', 'Uzman'),
        ('master', 'Usta'),
        ('legend', 'Efsane'),
        ('admin', 'Yönetici'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    title = models.CharField(max_length=100, blank=True, default="", verbose_name="Ünvan")
    location = models.CharField(max_length=100, blank=True, default="", verbose_name="Konum")
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES, default='Free')
    reputation = models.IntegerField(default=0, verbose_name="Akademik Puan")

    # Rütbe sistemi
    rank = models.CharField(max_length=20, choices=RANK_CHOICES, default='newbie', verbose_name="Rütbe")
    badges = models.ManyToManyField(Badge, blank=True, related_name='users', verbose_name="Rozetler")

    # EMAIL BİLDİRİM TERCİHLERİ
    email_on_reply = models.BooleanField(default=True, verbose_name="Konuma cevap geldiğinde email gönder")
    email_on_private_message = models.BooleanField(default=True, verbose_name="Özel mesaj geldiğinde email gönder")

    def __str__(self):
        return self.user.username

    def update_rank(self):
        """Puana göre rütbeyi otomatik günceller"""
        if self.user.is_superuser or self.user.is_staff:
            self.rank = 'admin'
        elif self.reputation >= 5000:
            self.rank = 'legend'
        elif self.reputation >= 2500:
            self.rank = 'master'
        elif self.reputation >= 1000:
            self.rank = 'expert'
        elif self.reputation >= 500:
            self.rank = 'contributor'
        elif self.reputation >= 200:
            self.rank = 'active'
        elif self.reputation >= 50:
            self.rank = 'member'
        else:
            self.rank = 'newbie'
        self.save(update_fields=['rank'])

    def get_rank_display_with_icon(self):
        """Rütbe adı ve ikonu ile birlikte döndürür"""
        rank_icons = {
            'newbie': ('🌱', '#94a3b8'),
            'member': ('👤', '#64748b'),
            'active': ('⚡', '#3b82f6'),
            'contributor': ('✍️', '#8b5cf6'),
            'expert': ('🎯', '#f59e0b'),
            'master': ('👑', '#ef4444'),
            'legend': ('🏆', '#eab308'),
            'admin': ('🛡️', '#dc2626'),
        }
        icon, color = rank_icons.get(self.rank, ('👤', '#64748b'))
        return {'icon': icon, 'color': color, 'name': self.get_rank_display()}

    def check_and_award_badges(self):
        """Puana göre otomatik rozet kontrolü ve ödüllendirme"""
        auto_badges = Badge.objects.filter(points_required__gt=0, points_required__lte=self.reputation)
        for badge in auto_badges:
            self.badges.add(badge)

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
