from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.urls import reverse
from .models import Post, PrivateMessage, Notification, PostLike

@receiver(post_save, sender=Post)
def post_save_receiver(sender, instance, created, **kwargs):
    if created and instance.topic.starter != instance.created_by:
        recipient = instance.topic.starter
        message = f"<b>{instance.created_by.username}</b>, '{instance.topic.subject}' konusuna yeni bir yanıt yazdı."
        url = instance.get_absolute_url()
        
        Notification.objects.create(
            recipient=recipient,
            sender=instance.created_by,
            verb=message,
            target=instance
        )
        
        channel_layer = get_channel_layer()
        group_name = f"notifications_{recipient.id}"
        
        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                "type": "notification_message",
                "message": message,
                "url": url,
            },
        )

@receiver(post_save, sender=PrivateMessage)
def private_message_post_save(sender, instance, created, **kwargs):
    if created:
        recipient = instance.receiver
        message = f"<b>{instance.sender.username}</b>'den yeni bir özel mesajınız var."
        url = reverse('inbox')

        Notification.objects.create(
            recipient=recipient,
            sender=instance.sender,
            verb=message,
            target=instance
        )

        channel_layer = get_channel_layer()
        group_name = f"notifications_{recipient.id}"

        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                'type': 'notification_message',
                'message': message,
                'url': url
            }
        )

@receiver(post_save, sender=PostLike)
def add_reputation_on_like(sender, instance, created, **kwargs):
    """Bir gönderi beğenildiğinde yazarına +5 puan ver"""
    if created:
        profile = instance.post.created_by.profile
        profile.reputation += 5
        profile.save()

@receiver(post_delete, sender=PostLike)
def remove_reputation_on_unlike(sender, instance, **kwargs):
    """Beğeni geri alınırsa puanı sil"""
    profile = instance.post.created_by.profile
    profile.reputation = max(0, profile.reputation - 5)
    profile.save()

@receiver(pre_save, sender=Post)
def capture_old_best_answer(sender, instance, **kwargs):
    """Post kaydedilmeden önceki 'is_best_answer' durumunu yakala"""
    if instance.pk:
        try:
            old_instance = Post.objects.get(pk=instance.pk)
            instance._old_is_best_answer = old_instance.is_best_answer
        except Post.DoesNotExist:
            pass

@receiver(post_save, sender=Post)
def handle_best_answer_reputation(sender, instance, created, **kwargs):
    """En iyi cevap seçildiğinde +20 puan ver, geri alınırsa sil"""
    if not created and hasattr(instance, '_old_is_best_answer'):
        if instance.is_best_answer and not instance._old_is_best_answer:
            profile = instance.created_by.profile
            profile.reputation += 20
            profile.save()
        elif not instance.is_best_answer and instance._old_is_best_answer:
            profile = instance.created_by.profile
            profile.reputation = max(0, profile.reputation - 20)
            profile.save()
