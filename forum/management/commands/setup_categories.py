from django.core.management.base import BaseCommand
from forum.models import Category  
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Forum kategorilerini otomatik oluşturur'

    def handle(self, *args, **kwargs):
        structure = [
            {
                "title": "YAZILIMLAR VE ARAÇLAR",
                "description": "Analiz için kullanılan programlar ve diller.",
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
                "description": "Metodoloji, test seçimi ve yorumlama.",
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
                "description": "Tez yazımı, kariyer ve yayın süreci.",
                "subs": [
                    {"title": "Araştırma Tasarımı", "description": "Örneklem hesabı, metodoloji belirleme."},
                    {"title": "Raporlama & Yazım", "description": "APA formatı, tez yazım kuralları."},
                    {"title": "Yayın Süreci", "description": "Dergi seçimi, hakem revizyonları."},
                    {"title": "Akademik Lounge", "description": "Sohbet, kariyer, motivasyon ve dertleşme."}
                ]
            }
        ]

        self.stdout.write("🚀 Kategoriler sizin mimarinize göre kuruluyor...")

        for main in structure:
            # Ana Kategori (Section'ı olmayan üst başlıklar)
            parent, created = Category.objects.get_or_create(
                title=main["title"],
                defaults={
                    'description': main["description"],
                    'slug': slugify(main["title"])
                }
            )
            
            # Alt Kategoriler (Section alanı parent'a bağlı)
            for sub in main["subs"]:
                Category.objects.get_or_create(
                    title=sub["title"],
                    section=parent, # Sizin modelde 'section' olarak geçiyor
                    defaults={
                        'description': sub["description"],
                        'slug': slugify(sub["title"])
                    }
                )

        self.stdout.write(self.style.SUCCESS('✨ ANALİZUS Kategorileri Mimarisi Tamamlandı!'))