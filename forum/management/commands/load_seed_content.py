import re
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from forum.models import Category, Topic, Post, Profile
from django.utils import timezone


class Command(BaseCommand):
    help = 'Forum seed content yükler (50 Q&A)'

    def handle(self, *args, **kwargs):
        self.stdout.write("📚 Seed content yükleme başlıyor...")

        # 1. Kullanıcı profillerini oluştur
        self.create_users()

        # 2. Seed content dosyasını oku
        self.load_content_from_file()

        self.stdout.write(self.style.SUCCESS('✅ Seed content başarıyla yüklendi!'))

    def create_users(self):
        """6 ana kullanıcı profilini oluşturur"""
        self.stdout.write("👥 Kullanıcılar oluşturuluyor...")

        users_data = [
            {
                'username': 'Dr_Mehmet_Stats',
                'email': 'mehmet@example.com',
                'first_name': 'Dr. Mehmet',
                'last_name': 'Yılmaz',
                'bio': 'İstatistik Doktorası (15+ yıl deneyim). SPSS, AMOS, Jamovi uzmanı.',
                'title': 'Doktor - İstatistik Uzmanı',
                'account_type': 'Expert'
            },
            {
                'username': 'PythonGurusu',
                'email': 'python@example.com',
                'first_name': 'Ayşe',
                'last_name': 'Demir',
                'bio': 'Veri Bilimci & Python Developer',
                'title': 'Veri Bilimci',
                'account_type': 'Expert'
            },
            {
                'username': 'R_Uzmani',
                'email': 'ruzmani@example.com',
                'first_name': 'Can',
                'last_name': 'Özkan',
                'bio': 'Ekonometri Araştırmacısı. R Studio, Zaman serisi, Regresyon uzmanı.',
                'title': 'Araştırmacı - Ekonometri',
                'account_type': 'Expert'
            },
            {
                'username': 'AnalizMeraklisi',
                'email': 'analiz@example.com',
                'first_name': 'Zeynep',
                'last_name': 'Kaya',
                'bio': 'Y. Lisans Öğrencisi (Eğitim Bilimleri)',
                'title': 'Y. Lisans Öğrencisi',
                'account_type': 'Premium'
            },
            {
                'username': 'TezDanismani_Prof',
                'email': 'prof@example.com',
                'first_name': 'Prof. Dr. Ali',
                'last_name': 'Arslan',
                'bio': 'Üniversite Profesörü (Psikoloji). Metodoloji, Nitel araştırma, Tez yazımı.',
                'title': 'Profesör - Psikoloji',
                'account_type': 'Expert'
            },
            {
                'username': 'MetodologiUzmani',
                'email': 'metodoloji@example.com',
                'first_name': 'Elif',
                'last_name': 'Şahin',
                'bio': 'Araştırma Görevlisi (Sosyoloji). Karma yöntem, SEM, Meta-analiz.',
                'title': 'Araştırma Görevlisi',
                'account_type': 'Premium'
            }
        ]

        # Soru soracak kullanıcılar (seed content'te geçenler)
        question_users = [
            'YeniAraştırmacı23', 'TezYolculugu2024', 'AnketUstasi', 'SosyalBilimci',
            'YeniBaslayan2024', 'AnketAnalisti', 'KavramKarmasasi', 'VeriTemizleyici',
            'ChartMerakli', 'SPSSYardım', 'RegresyonSorusu', 'MedyasyonSorunu',
            'PythonOgrenci', 'VeriKaziyici', 'MLOgreniyorum', 'RHataları',
            'GGPlotSorusu', 'KarmaYontemSorusu', 'SEMOgrencisi', 'MetaAnalizci',
            'OrneklemKrizi', 'GuvenilirlikSorusu', 'TezYazarken', 'LiteratürAvcısı',
            'APA7Karmasasi', 'EtikKurulSorusu', 'MakaleRevize', 'Doktora2024'
        ]

        for user_data in users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'email': user_data['email'],
                    'first_name': user_data['first_name'],
                    'last_name': user_data['last_name']
                }
            )
            if created:
                user.set_password('defaultpass123')
                user.save()

                # Profile oluştur
                Profile.objects.get_or_create(
                    user=user,
                    defaults={
                        'bio': user_data['bio'],
                        'title': user_data['title'],
                        'account_type': user_data['account_type']
                    }
                )
                self.stdout.write(f"  ✓ {user.username} oluşturuldu")

        # Soru soracak kullanıcıları oluştur
        for username in question_users:
            user, created = User.objects.get_or_create(
                username=username,
                defaults={'email': f'{username.lower()}@example.com'}
            )
            if created:
                user.set_password('defaultpass123')
                user.save()
                Profile.objects.get_or_create(user=user)

    def load_content_from_file(self):
        """AnalizDestek_Forum_Seed_Content.md dosyasını parse eder"""
        self.stdout.write("📄 Seed content dosyası okunuyor...")

        import os
        file_path = os.path.join(os.getcwd(), 'AnalizDestek_Forum_Seed_Content.md')

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Tüm soru bloklarını bul (## SORU ile başlayan)
        all_questions = re.findall(r'(## SORU \d+:.*?)(?=## SORU \d+:|# KULLANICI PROFİLLERİ|# ETİKET SİSTEMİ|$)', content, re.DOTALL)

        for question_block in all_questions:
            # Her soruyu ilgili kategoriye yönlendir
            self.parse_and_create_topic(question_block)

    def parse_and_create_topic(self, block):
        """Bir soru bloğunu parse edip Topic+Posts oluşturur"""

        # Başlık parse et (## SORU X: Başlık ✅ ÇÖZÜLDÜ)
        title_match = re.search(r'## SORU \d+: (.+?)(?:\s*✅ ÇÖZÜLDÜ)?\s*\n', block)
        if not title_match:
            return

        # Metadata parse et
        metadata = re.search(r'\*\*Başlık:\*\* (.+?)\n\*\*Kullanıcı:\*\* (.+?) \| \*\*Tarih:\*\* (.+?) \| \*\*Görüntülenme:\*\* (\d+)', block)
        if not metadata:
            return

        subject = metadata.group(1)
        username = metadata.group(2)
        date_str = metadata.group(3)
        views = int(metadata.group(4))

        # Etiketlerden kategoriyi belirle
        tags_match = re.search(r'\*\*Etiketler:\*\* (.+)', block)
        if not tags_match:
            return

        tags = tags_match.group(1)
        category = self.determine_category(tags)
        if not category:
            return

        # Kullanıcıyı bul
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # Yoksa oluştur
            user = User.objects.create_user(username=username, email=f'{username}@example.com', password='defaultpass123')
            Profile.objects.create(user=user)

        # Tarihi parse et (örn: "10 Ocak 2026")
        created_at = self.parse_turkish_date(date_str)

        # Soru içeriğini al
        question_match = re.search(r'\*\*Etiketler:\*\*.*?\n\n(.*?)(?=\n\*\*✅ EN FAYDA YANIT|\n---|\Z)', block, re.DOTALL)
        question_text = question_match.group(1).strip() if question_match else ""

        # Topic oluştur
        topic, created = Topic.objects.get_or_create(
            subject=subject,
            category=category,
            defaults={
                'starter': user,
                'views': views
            }
        )

        if created:
            topic.created_at = created_at
            topic.save()

            # İlk post (soru)
            Post.objects.create(
                topic=topic,
                message=question_text,
                created_by=user,
                created_at=created_at
            )

            # Cevapları ekle
            self.add_answers(topic, block, created_at)

            self.stdout.write(f"  ✓ {category.title}: {subject}")

    def determine_category(self, tags):
        """Etiketlerden kategoriyi belirler"""
        tags_lower = tags.lower()

        # Etiket bazlı kategori eşleştirme
        if any(tag in tags_lower for tag in ['#spss', '#amos', '#cronbach', '#normallik']):
            return Category.objects.filter(title='SPSS & AMOS').first()
        elif any(tag in tags_lower for tag in ['#python', '#pandas', '#machinelearning', '#veri']):
            return Category.objects.filter(title='Python & Veri Bilimi').first()
        elif any(tag in tags_lower for tag in ['#r ', '#rstudio', '#ggplot']):
            return Category.objects.filter(title='R Studio & İstatistik').first()
        elif any(tag in tags_lower for tag in ['#sem', '#metodoloji', '#örneklem', '#güvenilirlik', '#geçerlilik']):
            return Category.objects.filter(title='Metodoloji Tasarımı').first()
        elif any(tag in tags_lower for tag in ['#tez', '#makale', '#literatür', '#apa', '#etik', '#kongre']):
            return Category.objects.filter(title='Tez & Makale Yazımı').first()
        else:
            # Varsayılan: SPSS
            return Category.objects.filter(title='SPSS & AMOS').first()

    def add_answers(self, topic, block, question_date):
        """Bir topic'e cevapları ekler"""

        # En faydalı cevabı bul
        best_answer = re.search(r'\*\*✅ EN FAYDA YANIT\*\* \((.+?) - (\d+) beğeni\):\n(.*?)(?=\n\*\*|---|\Z)', block, re.DOTALL)

        if best_answer:
            answerer_username = best_answer.group(1)
            likes = int(best_answer.group(2))
            answer_text = best_answer.group(3).strip()

            try:
                answerer = User.objects.get(username=answerer_username)
            except User.DoesNotExist:
                answerer = User.objects.create_user(username=answerer_username, email=f'{answerer_username}@example.com', password='defaultpass123')
                Profile.objects.create(user=answerer)

            # Cevap 1-2 gün sonra gelmiş gibi yap
            answer_date = question_date + timedelta(hours=12)

            Post.objects.create(
                topic=topic,
                message=answer_text,
                created_by=answerer,
                created_at=answer_date,
                is_best_answer=True,
                likes=likes
            )

    def parse_turkish_date(self, date_str):
        """Türkçe tarih formatını parse eder (örn: '10 Ocak 2026')"""
        months = {
            'Ocak': 1, 'Şubat': 2, 'Mart': 3, 'Nisan': 4,
            'Mayıs': 5, 'Haziran': 6, 'Temmuz': 7, 'Ağustos': 8,
            'Eylül': 9, 'Ekim': 10, 'Kasım': 11, 'Aralık': 12
        }

        parts = date_str.strip().split()
        if len(parts) == 3:
            day = int(parts[0])
            month = months.get(parts[1], 1)
            year = int(parts[2])

            dt = datetime(year, month, day, 12, 0, 0)
            return timezone.make_aware(dt)

        return timezone.now()
