from django.core.management.base import BaseCommand
from forum.models import Section, Category  # İki modeli de çağırıyoruz
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Forum Section ve Category yapısını kurar'

    def handle(self, *args, **kwargs):
        # MİMARİ PLAN
        structure = [
            {
                "title": "YAZILIMLAR VE ARAÇLAR",
                "subs": [
                    {"title": "SPSS & AMOS", "description": "Sosyal bilimler analizleri ve YEM."},
                    {"title": "Python & Veri Bilimi", "description": "Pandas, NumPy, Scikit-Learn ve kodlama."},
                    {"title": "R Dili & R Studio", "description": "Akademik istatistik, ggplot2 ve paketler."},
                    {"title": "Excel & İş Zekası", "description": "İleri düzey formüller, PowerBI ve tablolar."},
                    {"title": "Nitel Analiz Araçları", "description": "NVivo, MAXQDA ve mülakat analizleri."},
                    {"title": "Diğer Araçlar", "description": "STATA, Minitab, MATLAB vb."}
                ]
            },
            {
                "title": "ANALİZ YÖNTEMLERİ",
                "subs": [
                    {"title": "Temel İstatistik", "description": "Veri temizleme, normallik, betimsel istatistik."},
                    {"title": "Hipotez Testleri", "description": "T-Testi, ANOVA, Mann Whitney U vb."},
                    {"title": "İlişki & Regresyon", "description": "Korelasyon, çoklu regresyon modelleri."},
                    {"title": "Ölçek Geliştirme", "description": "Geçerlilik (AFA/DFA), Güvenilirlik analizleri."},
                    {"title": "Yapay Zeka & DL", "description": "Makine öğrenmesi, sinir ağları, tahmin modelleri."}
                ]
            },
            {
                "title": "AKADEMİK DANIŞMA",
                "subs": [
                    {"title": "Araştırma Tasarımı", "description": "Örneklem hesabı, metodoloji belirleme."},
                    {"title": "Raporlama & Yazım", "description": "APA formatı, tez yazım kuralları."},
                    {"title": "Yayın Süreci", "description": "Dergi seçimi, hakem revizyonları."},
                    {"title": "Akademik Lounge", "description": "Sohbet, kariyer, motivasyon ve dertleşme."}
                ]
            }
        ]

        self.stdout.write("🚀 Veritabanı mimarisi kuruluyor...")

        # Döngüye bir sayaç (index) ekledik ki 'Section' sırasını (order) belirleyelim
        for index, main in enumerate(structure):
            
            # 1. ADIM: Önce SECTION (Ana Başlık) oluştur veya getir
            # order=index+1 diyerek sıralamayı veriyoruz (1, 2, 3...)
            section_obj, created = Section.objects.get_or_create(
                title=main["title"],
                defaults={'order': index + 1}
            )
            
            action = "Oluşturuldu" if created else "Zaten Vardı"
            self.stdout.write(f"📂 SECTION: {main['title']} ({action})")

            # 2. ADIM: Şimdi CATEGORY (Alt Başlık) oluştur ve Section'a bağla
            for sub in main["subs"]:
                Category.objects.get_or_create(
                    title=sub["title"],
                    section=section_obj,  # <--- İşte sihirli bağlantı burada!
                    defaults={
                        'description': sub["description"],
                        'slug': slugify(sub["title"].replace('ı', 'i').replace('İ', 'i')) # Türkçe karakter düzeltmesi
                    }
                )
                self.stdout.write(f"   - 📦 {sub['title']} eklendi.")

        self.stdout.write(self.style.SUCCESS('✨ TÜM BÖLÜMLER VE KATEGORİLER HAZIR KOMUTANIM!'))