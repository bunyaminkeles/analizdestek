from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from forum.models import Category, Topic, Post, Profile
import random

class Command(BaseCommand):
    help = 'Forum içeriğini SEO uyumlu soru-cevaplarla doldurur'

    def handle(self, *args, **kwargs):
        self.stdout.write("🚀 İçerik Operasyonu Başlıyor...")

        # 1. Bot Kullanıcıları Oluştur (Farklı kişiler soruyor gibi görünsün)
        bots = [
            {"username": "Dr_Veri", "title": "İstatistik Uzmanı"},
            {"username": "Acemi_Akademisyen", "title": "Doktora Öğrencisi"},
            {"username": "Analiz_Gurusu", "title": "Veri Bilimci"},
            {"username": "Tez_Magduru", "title": "Yüksek Lisans Öğrencisi"},
        ]
        
        user_objects = []
        for bot in bots:
            u, created = User.objects.get_or_create(username=bot['username'])
            if created:
                u.set_password("bot123")
                u.save()
                Profile.objects.create(user=u, title=bot['title'], account_type="Expert")
            user_objects.append(u)

        # 2. SEO Uyumlu İçerik Havuzu (Kategoriye Göre)
        # Format: (Kategori Başlığı Kısmı, Konu Başlığı, Konu Mesajı, Cevap Mesajı)
        contents = [
            # SPSS
            ("SPSS", "SPSS'te Normallik Testi (Kolmogorov vs Shapiro) hangisi?", 
             "Veri setim 45 kişi. Normallik testi yaparken Kolmogorov-Smirnov mu yoksa Shapiro-Wilk mi kullanmalıyım? Literatürde kafam karıştı.",
             "Merhaba Hocam. Örneklem sayınız 50'nin altında olduğu için (n<50) Shapiro-Wilk testi daha güçlü sonuç verir. Büyük örneklemlerde Kolmogorov tercih edilir. Ayrıca Skewness-Kurtosis değerlerine de bakmanızı öneririm."),
            
            ("SPSS", "Eksik verileri (Missing Value) nasıl atamalıyım?", 
             "Anket çalışmamda bazı katılımcılar soruları boş bırakmış. Ortalama atama mı yapayım yoksa o kişileri sileyim mi?",
             "Silmek veri kaybına yol açar. Eğer eksik veri %5'in altındaysa 'Series Mean' (Seri Ortalaması) atayabilirsiniz. Ancak daha profesyonel bir yaklaşım için SPSS'te 'Multiple Imputation' (Çoklu Atama) yöntemini kullanmanız daha bilimsel olur."),

            # Python
            ("Python", "Pandas ile Excel dosyasını okurken hata alıyorum", 
             "pd.read_excel komutunu kullanıyorum ama 'file not found' diyor. Dosya aynı klasörde.",
             "Dosya yolunu tam vermeyi deneyin veya klasör yapısında Türkçe karakter (ı, ğ, ş) olup olmadığını kontrol edin. Ayrıca 'openpyxl' kütüphanesinin yüklü olduğundan emin olun."),

            # R Studio
            ("R Dili", "ggplot2 grafikleri bulanık çıkıyor, nasıl düzeltirim?", 
             "R Studio'da çizdiğim grafikleri Word'e atınca kalitesi düşüyor. Yüksek çözünürlüklü nasıl kaydederim?",
             "Grafiklerinizi 'ggsave()' fonksiyonu ile kaydedin ve dpi=300 parametresini ekleyin. Örnek: ggsave('grafik.png', dpi=300). Bu sayede akademik baskı kalitesinde çıktı alırsınız."),

            # Hipotez Testleri
            ("Hipotez", "T-Testi mi yoksa Mann Whitney U mu?", 
             "İki grubum var ama verilerim normal dağılmadı. Hangi testi kullanmalıyım?",
             "Eğer verileriniz normal dağılım göstermiyorsa (Parametrik varsayımlar sağlanmıyorsa), Bağımsız Örneklem T-Testi yerine onun non-parametrik karşılığı olan Mann Whitney U testini kullanmalısınız."),

            ("Hipotez", "p değeri tam olarak 0.05 çıkarsa ne olur?", 
             "Analiz sonucumda p=0.050 çıktı. H0 reddedilir mi?",
             "Bu sınırda bir durumdur. Genelde p < 0.05 istenir. Tam 0.05 çıktığında güven aralığına bakmak gerekir. Ancak katı bir kural olarak p değeri 0.05'ten küçük olmalıdır, eşitse anlamlı kabul edilmeyebilir."),

            # Tez Yazımı
            ("Raporlama", "APA 7 formatına göre tablo nasıl yapılır?", 
             "Tezimde APA 7 kullanmam isteniyor. Tablolarda dikey çizgi kullanabilir miyim?",
             "APA 7 standartlarına göre tablolarda DİKEY çizgi (vertical lines) asla kullanılmaz. Sadece yatay çizgiler (en üst, başlık altı ve en alt) kullanılır. Sade bir görünüm esastır."),

            ("Yayın", "Predatory (Şaibeli) dergileri nasıl anlarım?", 
             "Bir dergiden mail geldi, 2 günde yayın garantisi veriyorlar. Güvenilir mi?",
             "Kesinlikle uzak durun Hocam. 'Hızlı yayın' ve 'Düşük ücret' vaadi genelde yağmacı dergi işaretidir. Derginin Web of Science veya Scopus indekslerinde tarandığını mutlaka kütüphane veritabanından teyit edin.")
        ]

        # 3. İçerikleri Veritabanına Bas
        for cat_key, subject, message, reply in contents:
            # Kategori bul (Title içinde geçen kelimeye göre)
            category = Category.objects.filter(title__icontains=cat_key).first()
            
            if category:
                starter = random.choice(user_objects)
                responder = random.choice([u for u in user_objects if u != starter])

                # Konuyu Oluştur
                topic, created = Topic.objects.get_or_create(
                    subject=subject,
                    category=category,
                    defaults={'starter': starter, 'views': random.randint(10, 500)}
                )

                if created:
                    # İlk mesajı at
                    Post.objects.create(topic=topic, author=starter, message=message)
                    self.stdout.write(f"✅ Konu Eklendi: {subject}")

                    # Cevabı at
                    Post.objects.create(topic=topic, author=responder, message=reply)
            else:
                self.stdout.write(self.style.WARNING(f"⚠️ Kategori Bulunamadı: {cat_key}"))

        self.stdout.write(self.style.SUCCESS('✨ TÜM SORU VE CEVAPLAR YÜKLENDİ KOMUTANIM!'))