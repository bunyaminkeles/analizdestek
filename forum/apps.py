from django.apps import AppConfig


class ForumConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forum'

    def ready(self):
        """
        Uygulama hazır olduğunda çalışır.
        Sinyallerimizi buraya import ederek Django'nun haberdar olmasını sağlarız.
        """
        import forum.signals
