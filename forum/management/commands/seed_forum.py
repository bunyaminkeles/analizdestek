import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
# HATA VEREN IMPORT KALDIRILDI, SADECE MODELLER KALDI:
from forum.models import Section, Category, Topic, Post, Profile
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Veritabanını temizler ve SEO uyumlu verilerle doldurur.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Veritabanı temizleniyor...'))

        # 1. TEMİZLİK (Eski verileri sil)
        # Hata almamak için sondan başa doğru siliyoruz (Post -> Topic -> Category -> Section)
        Post.objects.all().delete()
        Topic.objects.all().delete()
        Category.objects.all().delete()
        Section.objects.all().delete()

        # 2. SANAL KULLANICILAR VE PROFİLLER
        users = []
        user_data = [
            ('AnalizBot', 'Expert', 'Yapay Zeka Asistanı'),
            ('Dr_Istatistik', 'Expert', 'Doç. Dr. (Ekonometri)'),
            ('VeriGurusu', 'Premium', 'Data Scientist @ TechComp'),
            ('Akademik_Kus', 'Standard', 'Doktora Öğrencisi'),
            ('Arastirmaci01', 'Standard', 'Yüksek Lisans Öğrencisi')
        ]

        # Admin kullanıcısını da bulalım (varsa listeye ekleyelim)
        admin_user = User.objects.filter(is_superuser=True).first()
        
        for username, acc_type, title in user_data:
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password('pass1234')
                user.save()
            
            # Profil oluşturma (Varsa geç, yoksa yarat)
            # 500 hatasını önlemek için kritik adım
            if not hasattr(user, 'profile'):
                Profile.objects.create(user=user, account_type=acc_type, title=title)
            else:
                # Profil varsa güncelle
                user.profile.account_type = acc_type
                user.profile.title = title
                user.profile.save()
                
            users.append(user)

        if admin_user:
            users.append(admin_user)
            # Adminin profili yoksa ona da oluştur
            if not hasattr(admin_user, 'profile'):
                Profile.objects.create(user=admin_user, account_type='Admin', title='Sistem Yöneticisi')

        # 3. KATEGORİ AĞACI (VERİ YAPISI BURADA TANIMLANDI)
        structure = {
            "Nicel Analiz & İstatistik": [
                ("SPSS & AMOS", "bi-bar-chart-fill", "T-testi, ANOVA, Regresyon ve Yapısal Eşitlik Modellemesi."),
                ("R Studio & İstatistik", "bi-r-circle", "Akademik R paketleri, ggplot2 görselleştirme."),
                ("Python & Veri Bilimi", "bi-filetype-py", "Pandas, NumPy, Scikit-learn ile makine öğrenmesi."),
                ("Ekonometri & Stata", "bi-graph-up-arrow", "Zaman serileri ve panel veri analizi.")
            ],
            "Nitel Analiz & Araştırma": [
                ("NVivo & MAXQDA", "bi-chat-quote-fill", "Nitel veri kodlama ve tematik analiz."),
                ("Metodoloji Tasarımı", "bi-journal-richtext", "Örneklem seçimi ve anket hazırlama."),
                ("Tez & Makale Yazımı", "bi-pen-fill", "Akademik yazım kuralları ve dergi süreçleri.")
            ],
            "İş Zekası & Görselleştirme": [
                ("Power BI & Tableau", "bi-pie-chart-fill", "Dashboard tasarımı ve DAX formülleri."),
                ("Excel & İleri Düzey", "bi-grid-3x3-gap-fill", "VBA ve karmaşık Excel formülleri.")
            ],
            "Yapay Zeka & Gelecek": [
                ("LLM & Prompt Mühendisliği", "bi-robot", "ChatGPT, Claude ve akademik AI kullanımı.")
            ]
        }

        # 4. VERİLERİ OLUŞTUR
        for sec_title, categories in structure.items():
            section = Section.objects.create(title=sec_title)
            
            for cat_title, icon, desc in categories:
                # Slug oluştur
                slug_val = slugify(cat_title.replace('&', 've').replace('/', '-'))
                
                category = Category.objects.create(
                    section=section,
                    title=cat_title,
                    description=desc,
                    icon_class=icon,
                    slug=slug_val
                )

                # Örnek Konular
                topics_samples = [
                    f"{cat_title.split()[0]} ile analiz yaparken hata alıyorum",
                    "Veri setim normal dağılmıyor, ne yapmalıyım?",
                    "Hangi testi kullanacağıma karar veremedim",
                    f"{cat_title.split()[0]} raporlama formatı nasıl olmalı?"
                ]

                # Rastgele 2-4 konu ekle
                for t_title in random.sample(topics_samples, random.randint(2, 4)):
                    starter = random.choice(users)
                    topic = Topic.objects.create(
                        category=category,
                        subject=t_title,
                        starter=starter,
                        views=random.randint(10, 500)
                    )
                    
                    # İlk mesaj
                    Post.objects.create(
                        topic=topic,
                        author=starter,
                        message=f"Merhaba,\n\n**{t_title}** konusunda yardıma ihtiyacım var. Verilerim hazır ama analiz adımında takıldım.\n\nTeşekkürler."
                    )
                    
                    # Rastgele cevap
                    responder = random.choice(users)
                    if responder != starter:
                         Post.objects.create(
                            topic=topic,
                            author=responder,
                            message="Merhaba, veri setinizin detaylarını paylaşabilir misiniz?"
                        )

        self.stdout.write(self.style.SUCCESS('BAŞARILI! Veritabanı ve Profiller eksiksiz kuruldu.'))