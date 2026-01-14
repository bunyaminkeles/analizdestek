from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from forum.models import Category, Topic, Post, Profile
import random

class Command(BaseCommand):
    help = 'Foruma gerçek hayat senaryoları ve kaos anları ekler'

    def handle(self, *args, **kwargs):
        self.stdout.write("🔥 Kaos Senaryoları Yükleniyor...")

        # 1. Oyuncular (Gerçekçi Karakterler)
        actors = [
            {"username": "Panik_Atak_YLS", "title": "Tez Aşamasında"},
            {"username": "Dr_Sakin", "title": "Doçent Dr."},
            {"username": "Veri_Kashifi", "title": "Veri Analisti"},
            {"username": "Etik_Kurul_Zed", "title": "Araştırma Görevlisi"},
        ]
        
        user_objects = []
        for actor in actors:
            u, created = User.objects.get_or_create(username=actor['username'])
            if created:
                u.set_password("1234")
                u.save()
                Profile.objects.create(user=u, title=actor['title'], account_type="Standard")
            user_objects.append(u)

        # Uzmanlar (Cevap verenler)
        experts = User.objects.filter(username__in=["Dr_Veri", "Analiz_Gurusu", "AnalizBot"])
        if not experts.exists():
             # Eğer önceki script çalışmadıysa yedek uzman
             expert = User.objects.create(username="Dr_Mentor")
             experts = [expert]

        # 2. GERÇEK HAYAT SENARYOLARI (KAOS, DERT, POLİTİKA)
        scenarios = [
            # Kategori: Raporlama & Yazım
            ("Raporlama", 
             "Turnitin %24 çıktı, danışmanım 'Kabul etmem' diyor! Ne yapacağım?", 
             "Arkadaşlar acil yardım. Tezi bitirdim, Turnitin'e soktum %24 çıktı. Danışman sınır %20 dedi. Alıntılarım düzgün ama 'Benzerlik' yüksek çıkıyor. Kelime oyunlarıyla düşürsem etik dışı olur mu? Püf noktası var mı?",
             "Sakin olun hocam. %24 felaket bir oran değil. Öncelikle 'Bibliyografya' ve 'Doğrudan Alıntılar' (Tırnak içindekiler) rapordan çıkarıldı mı ona bakın. Filtre ayarlarından '5 kelimeden az eşleşmeleri çıkar' seçeneğini aktif ettirin. Sakın kelimelerin arasına görünmez karakter koymak gibi hilelere başvurmayın, diplomanız yanar. Cümle yapılarını değiştirerek (Paraphrasing) ilerleyin."),

            # Kategori: Hipotez Testleri
            ("Hipotez", 
             "Hipotezim desteklenmedi! Tezim çöp mü oldu?", 
             "Bütün literatür 'İlişki var' diyor, benim analizimde p=0.34 çıktı (Anlamsız). Dünyam başıma yıkıldı. Verilerle oynasam anlaşılır mı? Ya da tezi böyle versem jüri beni oyar mı?",
             "Sakın verilerle oynamayın (p-hacking), bu akademik sahtekarlıktır. Hipotezin desteklenmemesi de bilimsel bir bulgudur! 'Literatürün aksine, bu örneklemde ilişki bulunamamıştır' demek tezinizi çöp yapmaz, aksine özgün kılar. Tartışma kısmında neden çıkmamış olabileceğini (Örneklem kısıtı, kültürel fark vb.) güçlü savunursanız jüri daha çok takdir eder."),

            # Kategori: SPSS
            ("SPSS", 
             "SPSS 'Out of Memory' hatası veriyor, bilgisayarı kıracağım!", 
             "Elimde 2 milyon satırlık veri var. SPSS'te frekans alırken bile donuyor. RAM 16GB ama yetmiyor. SPSS'in bir ayarı var mı yoksa başka programa mı geçeyim?",
             "Hocam 2 milyon satır için SPSS (özellikle eski sürümler) hantal kalır. SPSS'in 'Edit > Options > Data' kısmından 'Calculate values before used' seçeneğini işaretleyip belleği biraz rahatlatabilirsiniz. Ama tavsiyem; bu boyutta veri için Python (Pandas) veya R (data.table) kullanmanızdır. İllaki SPSS derseniz, veriyi bölerek analiz yapmayı deneyin."),

            # Kategori: Akademik Lounge
            ("Akademik", 
             "Danışmanım maillerime 3 aydır cevap vermiyor...", 
             "Tez izleme raporu vereceğim, hoca ortada yok. Okula gidiyorum 'Toplantıda' diyorlar. Enstitüye şikayet etsem kariyerim biter mi? Danışman değiştirmek ne kadar zor?",
             "Çok hassas bir konu. Enstitüye resmi şikayet 'nükleer buton'dur, geri dönüşü olmaz ve hocalar arası dayanışma yüzünden siz zararlı çıkabilirsiniz. Önce Bölüm Başkanına 'Hocamla iletişim sorunu yaşıyoruz, ulaşamıyorum' diye sözlü (mail değil) danışın. Belki hocanın sağlık sorunu vs. vardır. Danışman değiştirmek hakkınızdır ama yeni hoca bulmadan eskisini bırakmayın."),

            # Kategori: Araştırma Tasarımı
            ("Araştırma", 
             "Anketime kimse cevap vermiyor, parayla veri toplasam etik mi?", 
             "400 kişi lazım, 3 aydır 120'de kaldım. Bir anket şirketi 'Biz 500 kişiye doldurturuz' dedi. Bunu yapsam tezimde 'Veriler online toplanmıştır' desem yalan olur mu?",
             "Anket şirketleri profesyonel paneller kullanıyorsa bu yasaldır ve etiktir. Ancak 'Kartopu örnekleme yaptım' deyip parayla toplattıysanız bu sorun olur. Metodoloji kısmında 'Veriler X Araştırma Şirketi paneli üzerinden toplanmıştır' diye dürüstçe yazarsanız hiçbir sorun olmaz. Bilimsel araştırmalarda bütçe kullanmak ayıp değildir."),
             
             # Kategori: Yapay Zeka
             ("Yapay Zeka", 
             "ChatGPT'ye literatür taraması yaptırdım, kaynaklar uydurma çıktı!", 
             "ChatGPT bana harika makaleler özetledi. Tam teze ekliyordum, kaynakçadaki makaleleri Google Scholar'da arattım, HİÇBİRİ YOK! Yapay zeka resmen makale uydurmuş. Bunu nasıl engellerim?",
             "Klasik 'AI Hallucination' vakası. ChatGPT bir arama motoru değildir, kelime tahmincisidir. Literatür için 'Consensus', 'Scite.ai' veya 'Elicit.org' gibi akademik AI araçlarını kullanmalısınız. Bunlar gerçek veritabanlarından (Semantic Scholar) veri çeker ve uydurmaz.")
        ]

        # 3. Veritabanına Bas
        for cat_key, subject, message, reply in scenarios:
            category = Category.objects.filter(title__icontains=cat_key).first()
            
            if category:
                starter = random.choice(user_objects)
                # Cevabı uzmanlardan biri versin
                responder = random.choice(list(experts))

                # Konuyu Oluştur
                topic, created = Topic.objects.get_or_create(
                    subject=subject,
                    category=category,
                    defaults={
                        'starter': starter, 
                        'views': random.randint(150, 1500), # Kaos konuları çok okunur
                        'is_pinned': False
                    }
                )

                if created:
                    # Soru (Panik)
                    Post.objects.create(topic=topic, author=starter, message=message)
                    self.stdout.write(f"🔥 Kaos Eklendi: {subject}")

                    # Cevap (Çözüm)
                    Post.objects.create(topic=topic, author=responder, message=reply)
            else:
                self.stdout.write(self.style.ERROR(f"Hata: {cat_key} kategorisi yok!"))

        self.stdout.write(self.style.SUCCESS('✨ TÜM SENARYOLAR BAŞARIYLA YÜKLENDİ!'))