from django.core.management.base import BaseCommand
from forum.models import Category  # DİKKAT: Senin Model ismin farklıysa burayı düzelt

class Command(BaseCommand):
    help = 'Forum kategorilerini otomatik oluşturur'

    def handle(self, *args, **kwargs):
        # KATEGORİ AĞACI (Senin onayladığın yapı)
        structure = [
            {
                "name": "YAZILIMLAR VE ARAÇLAR",
                "description": "Analiz için kullanılan programlar ve diller.",
                "children": [
                    {"name": "SPSS & AMOS", "description": "Sosyal bilimler analizleri ve YEM."},
                    {"name": "Python & Veri Bilimi", "description": "Pandas, NumPy, Scikit-Learn ve kodlama."},
                    {"name": "R Dili & R Studio", "description": "Akademik istatistik, ggplot2 ve paketler."},
                    {"name": "Excel & İş Zekası", "description": "İleri düzey formüller, PowerBI ve tablolar."},
                    {"name": "Nitel Analiz Araçları", "description": "NVivo, MAXQDA ve mülakat analizleri."},
                    {"name": "Diğer Araçlar", "description": "STATA, Minitab, MATLAB vb."}
                ]
            },
            {
                "name": "ANALİZ YÖNTEMLERİ",
                "description": "Metodoloji, test seçimi ve yorumlama.",
                "children": [
                    {"name": "Temel İstatistik", "description": "Veri temizleme, normallik, betimsel istatistik."},
                    {"name": "Hipotez Testleri", "description": "T-Testi, ANOVA, Mann Whitney U vb."},
                    {"name": "İlişki & Regresyon", "description": "Korelasyon, çoklu regresyon modelleri."},
                    {"name": "Ölçek Geliştirme", "description": "Geçerlilik (AFA/DFA), Güvenilirlik analizleri."},
                    {"name": "Yapay Zeka & DL", "description": "Makine öğrenmesi, sinir ağları, tahmin modelleri."}
                ]
            },
            {
                "name": "AKADEMİK DANIŞMA",
                "description": "Tez yazımı, kariyer ve yayın süreci.",
                "children": [
                    {"name": "Araştırma Tasarımı", "description": "Örneklem hesabı, metodoloji belirleme."},
                    {"name": "Raporlama & Yazım", "description": "APA formatı, tez yazım kuralları."},
                    {"name": "Yayın Süreci", "description": "Dergi seçimi, hakem revizyonları."},
                    {"name": "Akademik Lounge", "description": "Sohbet, kariyer, motivasyon ve dertleşme."}
                ]
            }
        ]

        self.stdout.write("🚀 Kategoriler kontrol ediliyor...")

        for main in structure:
            # Ana Kategori
            parent, created = Category.objects.get_or_create(
                name=main["name"],
                defaults={'description': main["description"]}
            )
            
            # Alt Kategoriler
            for child in main["children"]:
                Category.objects.get_or_create(
                    name=child["name"],
                    parent=parent,
                    defaults={'description': child["description"]}
                )

        self.stdout.write(self.style.SUCCESS('✨ TÜM KATEGORİLER HAZIR!'))