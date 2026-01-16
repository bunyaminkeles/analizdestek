import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from forum.models import Section, Category, Topic, Post, Profile
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Eksik kategorilere içerik ekler (mevcut verileri silmeden)'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Eksik içerikler ekleniyor...'))

        # Kullanıcıları al veya oluştur
        user_data = [
            ('VeriGorselci', 'Expert', 'Data Visualization Uzmanı'),
            ('MuhasebeUzmani', 'Premium', 'Finans Analisti'),
            ('Otomasyoncu', 'Premium', 'VBA & Makro Uzmanı'),
            ('Planlama_Y', 'Free', 'İş Planlama Uzmanı'),
            ('StratejiAnalisti', 'Expert', 'Business Intelligence'),
            ('Sosyolog_N', 'Expert', 'Dr. Nitel Araştırmacı'),
            ('GorselAnaliz', 'Premium', 'Etnograf'),
            ('Sahada_Arastirma', 'Free', 'Saha Araştırmacısı'),
            ('AkademikEtik', 'Expert', 'Araştırma Metodolojisti'),
            ('Iletisimci', 'Free', 'İletişim Uzmanı'),
            ('Ekonometrist', 'Expert', 'Doç. Dr. Ekonometri'),
            ('Muhendislik_R', 'Premium', 'Makine Mühendisi'),
            ('AI_Ogrenci', 'Free', 'YL Öğrencisi'),
            ('SaglikIst', 'Free', 'Sağlık İstatistikçisi'),
            ('Klinik_Aras', 'Expert', 'Dr. Klinik Araştırmacı'),
            ('Ekonometri_S', 'Premium', 'Ekonometri Uzmanı'),
            ('Psikoloji_Tez', 'Free', 'Doktora Öğrencisi'),
            ('Yonetim_Aras', 'Premium', 'İşletme Araştırmacısı'),
            ('Sosyal_Veri', 'Free', 'Sosyal Bilimci'),
            ('Literatur_Tarama', 'Expert', 'Bibliyometri Uzmanı'),
            ('Arastirmaci_X', 'Premium', 'Akademisyen'),
            ('Bilim_Haritaci', 'Free', 'Scientometrics'),
            ('AkademikKariyer', 'Free', 'Doktora Adayı'),
            ('YayinHedefi', 'Premium', 'Araştırmacı'),
            ('AnalizBot', 'Expert', 'AI Asistan'),
        ]

        users = {}
        for username, acc_type, title in user_data:
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password('pass1234')
                user.save()

            profile, _ = Profile.objects.get_or_create(user=user)
            profile.account_type = acc_type
            profile.title = title
            profile.save()

            users[username] = user

        # AnalizBot'u al
        analizbot = users.get('AnalizBot')

        # ===== EXCEL & İŞ ZEKASI İÇERİKLERİ =====
        excel_topics = [
            {
                'subject': "Excel'de otomatik güncellenen Dashboard nasıl yapılır?",
                'starter': 'VeriGorselci',
                'message': "Verilerimi her hafta güncelliyorum, grafiklerin manuel kaydırılmadan otomatik büyümesini nasıl sağlarım?",
                'answer': 'Verilerini "Tablo" (Ctrl+L) formatına sokmalısın. Grafik veri kaynağı tablo olursa, yeni veri eklediğinde grafik otomatik genişler. Pivot Table kullanıyorsan "Dilimleyici" (Slicer) eklemeyi unutma!',
                'views': 892,
            },
            {
                'subject': "10 farklı Excel dosyasını tek tabloda toplamak",
                'starter': 'MuhasebeUzmani',
                'message': "Farklı şubelerden gelen aylık raporları tek bir ana tabloda nasıl birleştiririm?",
                'answer': 'Veri sekmesinden "Verileri Al" > "Dosyadan" > "Klasörden" yolunu izle. Power Query tüm dosyaları sütun başlıklarına göre eşleştirip saniyeler içinde birleştirir.',
                'views': 1245,
            },
            {
                'subject': "Excel'de 'Makrolar devre dışı bırakıldı' hatası",
                'starter': 'Otomasyoncu',
                'message': "Yazdığım VBA kodları başka bilgisayarda çalışmıyor, neden?",
                'answer': 'Dosya > Seçenekler > Güven Merkezi > Makro Ayarları\'ndan "Tüm makroları etkinleştir" seçilmeli. Ayrıca dosyanın `.xlsx` değil, `.xlsm` formatında kaydedildiğinden emin ol.',
                'views': 756,
            },
            {
                'subject': "Hücre değerine göre tüm satırı renklendirme",
                'starter': 'Planlama_Y',
                'message': 'Sadece tek hücreyi değil, durum "Tamamlandı" ise tüm satırı yeşil yapmak istiyorum.',
                'answer': 'Koşullu Biçimlendirme > Yeni Kural > "Biçimlendirilecek hücreleri belirlemek için formül kullan" seç. Formüle `=$C2="Tamamlandı"` yaz (Dolar işareti sadece sütunda kalmalı).',
                'views': 634,
            },
            {
                'subject': "Büyük veri setleri için Excel yeterli mi?",
                'starter': 'StratejiAnalisti',
                'message': "1 milyon satırın üzerindeki verilerde Excel çok kasıyor, Power BI'a geçmeli miyim?",
                'answer': "Kesinlikle evet. Excel'in satır limiti 1.048.576'dır. Power BI ise \"Veri Modeli\" mimarisiyle milyonlarca satırı saniyeler içinde işleyebilir.",
                'views': 1567,
            },
        ]

        # ===== NİTEL ANALİZ ARAÇLARI İÇERİKLERİ =====
        nitel_topics = [
            {
                'subject': "Mülakat metinlerini kodlarken nelere dikkat edilmeli?",
                'starter': 'Sosyolog_N',
                'message': "MAXQDA'da çok fazla kod oluşturmak analizi zorlaştırır mı?",
                'answer': 'Başlangıçta "Açık Kodlama" yaparken cömert olabilirsin ama sonra bu kodları hiyerarşik temalar altında toplamalısın. "Kod Ağacı" çok karmaşıksa analizde kaybolabilirsin.',
                'views': 423,
            },
            {
                'subject': "NVivo ile fotoğraf ve video kodlanabilir mi?",
                'starter': 'GorselAnaliz',
                'message': "Etnografik çalışmamda fotoğrafları analiz birimi olarak kullanabilir miyim?",
                'answer': "Evet, NVivo'da resim dosyalarını içe aktarıp belirli bölgeleri (region) kare içine alarak kodlayabilirsin. Her bölgeye ayrı notlar eklemek mümkün.",
                'views': 312,
            },
            {
                'subject': "Ses kayıtlarını metne dönüştüren en iyi araç hangisi?",
                'starter': 'Sahada_Arastirma',
                'message': "Mülakatları tek tek elle yazmak çok vakit alıyor. Yapay zeka çözümü var mı?",
                'answer': 'Türkçe için "Otter.ai" zayıf kalsa da, "Whisper AI" veya yerli "Voiser" oldukça başarılı. Metne çevirdikten sonra MAXQDA\'ya `.docx` olarak aktarabilirsin.',
                'views': 867,
            },
            {
                'subject': "İki farklı kodlayıcı arasındaki uyum (Inter-coder Reliability)",
                'starter': 'AkademikEtik',
                'message': "Aynı metni iki kişi kodladık, uyum oranını nasıl raporlamalıyız?",
                'answer': 'MAXQDA içinde "Kullanıcılar Arası Uyumu Kontrol Et" aracı vardır. Cohen\'s Kappa katsayısının 0.70 üzerinde olması akademik olarak kabul edilebilirdir.',
                'views': 534,
            },
            {
                'subject': "En sık geçen kavramları görselleştirme",
                'starter': 'Iletisimci',
                'message': "Odak grup görüşmelerinde en çok kullanılan kelimeleri nasıl raporlarım?",
                'answer': '"Kelime Bulutu" (Word Cloud) aracını kullan. Ancak "ve, ama, gibi" gibi anlam taşımayan kelimeleri "Stop Word List" (Hariç Tutulanlar) listesine eklemeyi unutma.',
                'views': 445,
            },
        ]

        # ===== DİĞER ARAÇLAR (STATA, MATLAB) İÇERİKLERİ =====
        stata_topics = [
            {
                'subject': "Panel veride Fixed Effects vs Random Effects?",
                'starter': 'Ekonometrist',
                'message': "Hangisini seçeceğime nasıl karar veririm?",
                'answer': "Stata'da `hausman` testini kullanmalısın. Eğer p < 0.05 ise Fixed Effects (Sabit Etkiler) modelini kullanman gerekir.",
                'views': 1123,
            },
            {
                'subject': "MATLAB plot renklerini ve kalınlıklarını ayarlama",
                'starter': 'Muhendislik_R',
                'message': "Makale için yüksek çözünürlüklü grafik çıktısı nasıl alınır?",
                'answer': "`plot(x,y,'LineWidth',2,'Color','r')` komutunu kullan. Çıktı alırken `exportgraphics` fonksiyonu ile 300 DPI çözünürlükte `.tiff` veya `.pdf` kaydet.",
                'views': 678,
            },
            {
                'subject': "Analizlerimi neden Do-File ile kaydetmeliyim?",
                'starter': 'Ekonometrist',
                'message': "Komut penceresinden yazmak daha hızlı değil mi?",
                'answer': 'Hayır, Do-File analizin "kara kutusu"dur. Hata yaptığında veya hakem düzeltme istediğinde tek tıkla her şeyi en baştan hatasız çalıştırabilirsin.',
                'views': 534,
            },
            {
                'subject': "MATLAB ile hazır yapay zeka modelleri kullanılabilir mi?",
                'starter': 'AI_Ogrenci',
                'message': "Resim sınıflandırma için hazır modeller var mı?",
                'answer': '"Deep Learning Toolbox" içinde AlexNet, GoogLeNet gibi önceden eğitilmiş modelleri saniyeler içinde çağırıp kendi verilerinle "Transfer Learning" yapabilirsin.',
                'views': 892,
            },
            {
                'subject': "Eksik verileri (Missing Values) toplu silme",
                'starter': 'SaglikIst',
                'message': "`drop if missing(var)` komutu güvenli mi?",
                'answer': 'Güvenlidir ancak veri kaybına yol açar. Önce `mdesc` komutuyla eksiklik oranına bak, eğer oran %5\'ten azsa silebilirsin, fazlaysa "Multiple Imputation" yöntemini düşün.',
                'views': 445,
            },
        ]

        # ===== İLİŞKİ & REGRESYON İÇERİKLERİ =====
        regresyon_topics = [
            {
                'subject': "Odds Ratio (Olasılıklar Oranı) nedir?",
                'starter': 'Klinik_Aras',
                'message': "Lojistik regresyon sonucunda çıkan Exp(B) değerini nasıl okurum?",
                'answer': "Exp(B) > 1 ise bağımsız değişken bağımlı değişkenin gerçekleşme olasılığını artırıyor demektir. Örneğin 1.50 çıktıysa, o durumun görülme olasılığı %50 artıyor demektir.",
                'views': 1456,
            },
            {
                'subject': "VIF değerleri kaç olmalı?",
                'starter': 'Ekonometri_S',
                'message': "Bağımsız değişkenlerim birbirine çok benziyor, model bozulur mu?",
                'answer': "VIF değerlerine bak. VIF > 10 ise ciddi bir çoklu doğrusal bağlantı sorunu vardır. Akademik olarak genellikle 5'in altı istenir.",
                'views': 1234,
            },
            {
                'subject': "Baron ve Kenny yöntemi hala geçerli mi?",
                'starter': 'Psikoloji_Tez',
                'message': "Danışmanım Process Macro kullanmamı istiyor, farkı nedir?",
                'answer': "Baron-Kenny artık eskidi. Hayes'in **Process Macro**su (Bootstrap yöntemi) çok daha güçlü ve modern kabul ediliyor. Model 4 en yaygın aracılık modelidir.",
                'views': 1678,
            },
            {
                'subject': "Etkileşim terimi (Interaction Term) nasıl oluşturulur?",
                'starter': 'Yonetim_Aras',
                'message': "Cinsiyetin eğitimin maaş üzerindeki etkisini değiştirdiğini nasıl test ederim?",
                'answer': "Eğitim ve Cinsiyet değişkenlerini çarparak yeni bir değişken oluşturmalısın. Eğer bu çarpım terimi regresyonda anlamlı çıkarsa, moderasyon etkisi vardır.",
                'views': 987,
            },
            {
                'subject': "Kategorik değişkenler regresyona nasıl girer?",
                'starter': 'Sosyal_Veri',
                'message': "Eğitim durumu (Lise, Lisans, Lisansüstü) değişkenini nasıl modele eklerim?",
                'answer': 'n-1 kuralını uygula. 3 kategorin varsa 2 adet kukla değişken oluşturmalısın. Bir kategoriyi "Referans" olarak dışarıda bırakmalısın.',
                'views': 756,
            },
        ]

        # ===== BİBLİYOMETRİK ANALİZLER İÇERİKLERİ =====
        biblio_topics = [
            {
                'subject': "Bibliyometrik görselleştirme için hangi araç daha iyi?",
                'starter': 'Literatur_Tarama',
                'message': "VOSviewer vs Biblioshiny - Görsel olarak hangisi makalelerde daha çok kabul görüyor?",
                'answer': "VOSviewer ağ haritaları için standarttır. Biblioshiny (R-Bibliometrix) ise daha detaylı istatistiksel tablolar sunar. İkisini birden kullanmak en iyisidir.",
                'views': 1123,
            },
            {
                'subject': "Hangi veri tabanı bibliyometride daha kapsayıcı?",
                'starter': 'Arastirmaci_X',
                'message': "Scopus mu Web of Science mı? İki veriyi birleştirebilir miyim?",
                'answer': "Scopus genellikle daha fazla dergi içerir ama WoS daha prestijli kabul edilir. İkisini birleştirmek zordur (mükerrer kayıtlar yüzünden), genellikle tek bir tanesi seçilir.",
                'views': 987,
            },
            {
                'subject': "Ortak atıf ile ortak yazarlık arasındaki fark nedir?",
                'starter': 'Bilim_Haritaci',
                'message': "Hangi analiz entelektüel yapıyı gösterir?",
                'answer': "Co-citation analizi, iki makalenin aynı anda üçüncü bir makale tarafından kaynak gösterilmesidir. Bu, o alanın teorik temellerini ortaya çıkarır.",
                'views': 756,
            },
            {
                'subject': "Bir yazarın etkisini ölçmek için sadece H-indeksi yeterli mi?",
                'starter': 'AkademikKariyer',
                'message': "i10 indeksi ne işe yarar?",
                'answer': "H-indeksi nicelik ve niteliği birleştirir ama yeni yazarlar için dezavantajlıdır. i10 indeksi ise Google Scholar'ın kullandığı, en az 10 atıf almış makale sayısını gösteren bir metriktir.",
                'views': 645,
            },
            {
                'subject': "Sadece bibliyometrik analiz ile Q1 dergide yayın yapılır mı?",
                'starter': 'YayinHedefi',
                'message': "Sadece grafik koymak yeterli mi?",
                'answer': 'Hayır. Grafiklerin ötesine geçip alanın "gelecek projeksiyonunu" yapmalı, boşlukları (research gaps) belirlemeli ve derinlemesine bir tartışma sunmalısın.',
                'views': 1234,
            },
        ]

        # Kategori slug eşleştirmeleri (canlı siteye göre)
        category_content_map = {
            'excel-is-zekasi': excel_topics,
            'excel-ve-is-zekasi': excel_topics,
            'nitel-analiz-araclari': nitel_topics,
            'diger-araclar': stata_topics,
            'iliski-regresyon': regresyon_topics,
            'iliski-ve-regresyon': regresyon_topics,
            'bibliometrik-analizler': biblio_topics,
        }

        added_topics = 0
        added_posts = 0

        for category in Category.objects.all():
            slug = category.slug
            topics_data = None

            # Slug eşleştirmesi
            for key, data in category_content_map.items():
                if key in slug or slug in key:
                    topics_data = data
                    break

            if topics_data and category.topics.count() == 0:
                self.stdout.write(f"  → {category.title} kategorisine içerik ekleniyor...")

                for topic_data in topics_data:
                    starter = users.get(topic_data['starter'], analizbot)

                    topic = Topic.objects.create(
                        category=category,
                        subject=topic_data['subject'],
                        starter=starter,
                        views=topic_data.get('views', random.randint(100, 500))
                    )
                    added_topics += 1

                    # Soru
                    Post.objects.create(
                        topic=topic,
                        created_by=starter,
                        message=f"Merhaba,\n\n{topic_data['message']}\n\nTeşekkürler."
                    )
                    added_posts += 1

                    # Cevap
                    Post.objects.create(
                        topic=topic,
                        created_by=analizbot,
                        message=f"Merhaba,\n\n{topic_data['answer']}\n\nBaşarılar dilerim!",
                        is_best_answer=True
                    )
                    added_posts += 1

        # İstatistikleri göster
        total_topics = Topic.objects.count()
        total_posts = Post.objects.count()

        self.stdout.write(self.style.SUCCESS(f'''
╔══════════════════════════════════════════════╗
║     ✅ EKSİK İÇERİKLER EKLENDİ!              ║
╠══════════════════════════════════════════════╣
║  ➕ Eklenen Konu: {added_topics:<25} ║
║  ➕ Eklenen Gönderi: {added_posts:<22} ║
║  📊 Toplam Konu: {total_topics:<26} ║
║  💬 Toplam Gönderi: {total_posts:<23} ║
╚══════════════════════════════════════════════╝
        '''))
