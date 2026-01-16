from django.core.management.base import BaseCommand
from forum.models import Skill


class Command(BaseCommand):
    help = 'Varsayılan uzmanlık alanlarını (skill) oluşturur'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Uzmanlık alanları oluşturuluyor...'))

        skills_data = [
            # === İSTATİSTİK YAZILIMLARI ===
            {'name': 'SPSS', 'slug': 'spss', 'icon': 'bi-bar-chart-fill', 'color': '#e74c3c', 'category': 'Yazılım'},
            {'name': 'AMOS', 'slug': 'amos', 'icon': 'bi-diagram-3', 'color': '#9b59b6', 'category': 'Yazılım'},
            {'name': 'STATA', 'slug': 'stata', 'icon': 'bi-graph-up-arrow', 'color': '#3498db', 'category': 'Yazılım'},
            {'name': 'Minitab', 'slug': 'minitab', 'icon': 'bi-pie-chart', 'color': '#27ae60', 'category': 'Yazılım'},
            {'name': 'Eviews', 'slug': 'eviews', 'icon': 'bi-graph-down', 'color': '#f39c12', 'category': 'Yazılım'},
            {'name': 'LISREL', 'slug': 'lisrel', 'icon': 'bi-bezier2', 'color': '#1abc9c', 'category': 'Yazılım'},
            {'name': 'SmartPLS', 'slug': 'smartpls', 'icon': 'bi-diagram-2', 'color': '#e67e22', 'category': 'Yazılım'},

            # === PROGRAMLAMA DİLLERİ ===
            {'name': 'Python', 'slug': 'python', 'icon': 'bi-filetype-py', 'color': '#3776ab', 'category': 'Programlama'},
            {'name': 'R', 'slug': 'r', 'icon': 'bi-r-circle', 'color': '#276dc3', 'category': 'Programlama'},
            {'name': 'MATLAB', 'slug': 'matlab', 'icon': 'bi-cpu', 'color': '#0076a8', 'category': 'Programlama'},
            {'name': 'SQL', 'slug': 'sql', 'icon': 'bi-database', 'color': '#00758f', 'category': 'Programlama'},
            {'name': 'Julia', 'slug': 'julia', 'icon': 'bi-code-slash', 'color': '#9558b2', 'category': 'Programlama'},

            # === NİTEL ANALİZ ===
            {'name': 'NVivo', 'slug': 'nvivo', 'icon': 'bi-chat-quote', 'color': '#2ecc71', 'category': 'Nitel'},
            {'name': 'MAXQDA', 'slug': 'maxqda', 'icon': 'bi-chat-text', 'color': '#e74c3c', 'category': 'Nitel'},
            {'name': 'Atlas.ti', 'slug': 'atlasti', 'icon': 'bi-file-text', 'color': '#3498db', 'category': 'Nitel'},

            # === VERİ BİLİMİ ===
            {'name': 'Machine Learning', 'slug': 'ml', 'icon': 'bi-robot', 'color': '#8e44ad', 'category': 'AI'},
            {'name': 'Deep Learning', 'slug': 'dl', 'icon': 'bi-layers', 'color': '#9b59b6', 'category': 'AI'},
            {'name': 'NLP', 'slug': 'nlp', 'icon': 'bi-chat-dots', 'color': '#1abc9c', 'category': 'AI'},
            {'name': 'Computer Vision', 'slug': 'cv', 'icon': 'bi-eye', 'color': '#e67e22', 'category': 'AI'},
            {'name': 'TensorFlow', 'slug': 'tensorflow', 'icon': 'bi-gpu-card', 'color': '#ff6f00', 'category': 'AI'},
            {'name': 'PyTorch', 'slug': 'pytorch', 'icon': 'bi-fire', 'color': '#ee4c2c', 'category': 'AI'},

            # === BİBLİYOMETRİ ===
            {'name': 'VOSviewer', 'slug': 'vosviewer', 'icon': 'bi-share', 'color': '#3498db', 'category': 'Bibliyometri'},
            {'name': 'Biblioshiny', 'slug': 'biblioshiny', 'icon': 'bi-book', 'color': '#2ecc71', 'category': 'Bibliyometri'},
            {'name': 'CiteSpace', 'slug': 'citespace', 'icon': 'bi-globe', 'color': '#e74c3c', 'category': 'Bibliyometri'},

            # === ANALİZ YÖNTEMLERİ ===
            {'name': 'Regresyon Analizi', 'slug': 'regression', 'icon': 'bi-graph-up', 'color': '#3498db', 'category': 'Yöntem'},
            {'name': 'Faktör Analizi', 'slug': 'factor-analysis', 'icon': 'bi-grid-3x3', 'color': '#9b59b6', 'category': 'Yöntem'},
            {'name': 'Yapısal Eşitlik', 'slug': 'sem', 'icon': 'bi-diagram-3-fill', 'color': '#e74c3c', 'category': 'Yöntem'},
            {'name': 'Panel Veri', 'slug': 'panel-data', 'icon': 'bi-table', 'color': '#2ecc71', 'category': 'Yöntem'},
            {'name': 'Zaman Serisi', 'slug': 'time-series', 'icon': 'bi-clock-history', 'color': '#f39c12', 'category': 'Yöntem'},
            {'name': 'Meta Analiz', 'slug': 'meta-analysis', 'icon': 'bi-collection', 'color': '#1abc9c', 'category': 'Yöntem'},
            {'name': 'Ölçek Geliştirme', 'slug': 'scale-dev', 'icon': 'bi-rulers', 'color': '#e67e22', 'category': 'Yöntem'},

            # === VERİ GÖRSELLEŞTİRME ===
            {'name': 'Tableau', 'slug': 'tableau', 'icon': 'bi-pie-chart-fill', 'color': '#e97627', 'category': 'Görselleştirme'},
            {'name': 'Power BI', 'slug': 'powerbi', 'icon': 'bi-bar-chart-line', 'color': '#f2c811', 'category': 'Görselleştirme'},
            {'name': 'Excel', 'slug': 'excel', 'icon': 'bi-file-earmark-spreadsheet', 'color': '#217346', 'category': 'Görselleştirme'},
            {'name': 'ggplot2', 'slug': 'ggplot2', 'icon': 'bi-palette', 'color': '#276dc3', 'category': 'Görselleştirme'},
        ]

        created_count = 0
        updated_count = 0

        for skill_data in skills_data:
            skill, created = Skill.objects.update_or_create(
                slug=skill_data['slug'],
                defaults=skill_data
            )
            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(self.style.SUCCESS(f'''
╔══════════════════════════════════════════════╗
║     🎯 UZMANLIK ALANLARI HAZIR!              ║
╠══════════════════════════════════════════════╣
║  ✨ Yeni Yetenek: {created_count:<25} ║
║  🔄 Güncellenen: {updated_count:<26} ║
║  📊 Toplam Yetenek: {Skill.objects.count():<23} ║
╚══════════════════════════════════════════════╝
        '''))
