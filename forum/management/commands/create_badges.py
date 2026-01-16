from django.core.management.base import BaseCommand
from forum.models import Badge, Profile


class Command(BaseCommand):
    help = 'Varsayılan rozetleri oluşturur'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Rozetler oluşturuluyor...'))

        badges_data = [
            # === BAŞARI ROZETLERİ (Puana göre otomatik) ===
            {
                'name': 'İlk Adım',
                'slug': 'ilk-adim',
                'description': 'Foruma ilk katkınızı yaptınız!',
                'icon': 'bi-emoji-smile',
                'color': '#22c55e',
                'badge_type': 'achievement',
                'points_required': 10,
            },
            {
                'name': 'Yükselen Yıldız',
                'slug': 'yukselen-yildiz',
                'description': '50 puan kazandınız',
                'icon': 'bi-star',
                'color': '#3b82f6',
                'badge_type': 'achievement',
                'points_required': 50,
            },
            {
                'name': 'Aktif Katılımcı',
                'slug': 'aktif-katilimci',
                'description': '200 puan kazandınız',
                'icon': 'bi-lightning',
                'color': '#8b5cf6',
                'badge_type': 'achievement',
                'points_required': 200,
            },
            {
                'name': 'Bilgi Kaynağı',
                'slug': 'bilgi-kaynagi',
                'description': '500 puan kazandınız',
                'icon': 'bi-book',
                'color': '#f59e0b',
                'badge_type': 'achievement',
                'points_required': 500,
            },
            {
                'name': 'Uzman',
                'slug': 'uzman',
                'description': '1000 puan kazandınız',
                'icon': 'bi-mortarboard',
                'color': '#ef4444',
                'badge_type': 'achievement',
                'points_required': 1000,
            },
            {
                'name': 'Profesör',
                'slug': 'profesor',
                'description': '2500 puan kazandınız',
                'icon': 'bi-award',
                'color': '#dc2626',
                'badge_type': 'achievement',
                'points_required': 2500,
            },
            {
                'name': 'Efsane',
                'slug': 'efsane',
                'description': '5000 puan kazandınız',
                'icon': 'bi-trophy',
                'color': '#eab308',
                'badge_type': 'achievement',
                'points_required': 5000,
            },

            # === UZMANLIK ROZETLERİ (Manuel verilir) ===
            {
                'name': 'SPSS Uzmanı',
                'slug': 'spss-uzmani',
                'description': 'SPSS konusunda uzman',
                'icon': 'bi-bar-chart-fill',
                'color': '#0ea5e9',
                'badge_type': 'specialty',
                'points_required': 0,
            },
            {
                'name': 'Python Gurusu',
                'slug': 'python-gurusu',
                'description': 'Python ve veri bilimi uzmanı',
                'icon': 'bi-filetype-py',
                'color': '#3b82f6',
                'badge_type': 'specialty',
                'points_required': 0,
            },
            {
                'name': 'R Wizard',
                'slug': 'r-wizard',
                'description': 'R ve istatistik uzmanı',
                'icon': 'bi-graph-up',
                'color': '#2563eb',
                'badge_type': 'specialty',
                'points_required': 0,
            },
            {
                'name': 'Yapay Zeka Araştırmacısı',
                'slug': 'ai-arastirmaci',
                'description': 'AI ve ML konularında uzman',
                'icon': 'bi-robot',
                'color': '#7c3aed',
                'badge_type': 'specialty',
                'points_required': 0,
            },
            {
                'name': 'Nitel Analiz Uzmanı',
                'slug': 'nitel-uzman',
                'description': 'MAXQDA, NVivo uzmanı',
                'icon': 'bi-chat-quote',
                'color': '#059669',
                'badge_type': 'specialty',
                'points_required': 0,
            },
            {
                'name': 'Ekonometrist',
                'slug': 'ekonometrist',
                'description': 'Ekonometri ve Stata uzmanı',
                'icon': 'bi-currency-dollar',
                'color': '#16a34a',
                'badge_type': 'specialty',
                'points_required': 0,
            },

            # === KATILIM ROZETLERİ ===
            {
                'name': 'Yardımsever',
                'slug': 'yardimsever',
                'description': '10 soruya cevap verdi',
                'icon': 'bi-heart',
                'color': '#ec4899',
                'badge_type': 'participation',
                'points_required': 0,
            },
            {
                'name': 'En İyi Cevap',
                'slug': 'en-iyi-cevap',
                'description': 'Cevabı "En Faydalı" seçildi',
                'icon': 'bi-check-circle',
                'color': '#22c55e',
                'badge_type': 'participation',
                'points_required': 0,
            },
            {
                'name': 'Popüler Yazar',
                'slug': 'populer-yazar',
                'description': 'Konusu 1000+ görüntülendi',
                'icon': 'bi-eye',
                'color': '#f97316',
                'badge_type': 'participation',
                'points_required': 0,
            },

            # === ÖZEL ROZETLER ===
            {
                'name': 'Kurucu Üye',
                'slug': 'kurucu-uye',
                'description': 'Platform kuruluş döneminde katıldı',
                'icon': 'bi-gem',
                'color': '#a855f7',
                'badge_type': 'special',
                'points_required': 0,
            },
            {
                'name': 'Beta Tester',
                'slug': 'beta-tester',
                'description': 'Beta testine katıldı',
                'icon': 'bi-bug',
                'color': '#06b6d4',
                'badge_type': 'special',
                'points_required': 0,
            },
            {
                'name': 'Moderatör',
                'slug': 'moderator',
                'description': 'Forum moderatörü',
                'icon': 'bi-shield-check',
                'color': '#dc2626',
                'badge_type': 'special',
                'points_required': 0,
            },
            {
                'name': 'Doğrulanmış Akademisyen',
                'slug': 'dogrulanmis-akademisyen',
                'description': 'Akademik kimliği doğrulandı',
                'icon': 'bi-patch-check',
                'color': '#0ea5e9',
                'badge_type': 'special',
                'points_required': 0,
            },
        ]

        created_count = 0
        updated_count = 0

        for badge_data in badges_data:
            badge, created = Badge.objects.update_or_create(
                slug=badge_data['slug'],
                defaults=badge_data
            )
            if created:
                created_count += 1
            else:
                updated_count += 1

        # Mevcut kullanıcılara puana göre rozet ver
        self.stdout.write('Kullanıcılara otomatik rozetler veriliyor...')
        for profile in Profile.objects.all():
            profile.check_and_award_badges()
            profile.update_rank()

        self.stdout.write(self.style.SUCCESS(f'''
╔══════════════════════════════════════════════╗
║     🏆 ROZET SİSTEMİ HAZIR!                  ║
╠══════════════════════════════════════════════╣
║  ✨ Yeni Rozet: {created_count:<27} ║
║  🔄 Güncellenen: {updated_count:<26} ║
║  📊 Toplam Rozet: {Badge.objects.count():<25} ║
╚══════════════════════════════════════════════╝
        '''))
