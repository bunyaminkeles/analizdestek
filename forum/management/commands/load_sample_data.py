"""
Örnek veri yükleme komutu
Kullanım: python manage.py load_sample_data
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from forum.models import Section, Category, Topic, Post, Profile, DailyTip, QuizQuestion


class Command(BaseCommand):
    help = 'Örnek veriler yükler (kategoriler, konular, ipuçları, quiz)'

    def handle(self, *args, **options):
        self.stdout.write('Örnek veriler yükleniyor...')

        # 1. Admin kullanıcı oluştur
        admin, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@analizus.com',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            admin.set_password('admin123')
            admin.save()
            Profile.objects.get_or_create(user=admin)
            self.stdout.write(self.style.SUCCESS('Admin kullanıcı oluşturuldu'))

        # 2. Uzman kullanıcılar
        experts = [
            ('Dr_Mehmet_Stats', 'mehmet@example.com'),
            ('PythonGurusu', 'python@example.com'),
            ('R_Uzmani', 'r@example.com'),
            ('TezDanismani_Prof', 'prof@example.com'),
            ('SPSSUzmani', 'spss@example.com'),
        ]
        expert_users = []
        for username, email in experts:
            user, created = User.objects.get_or_create(
                username=username,
                defaults={'email': email}
            )
            if created:
                user.set_password('test123')
                user.save()
                Profile.objects.get_or_create(user=user)
            expert_users.append(user)
        self.stdout.write(self.style.SUCCESS(f'{len(experts)} uzman kullanıcı oluşturuldu'))

        # 3. Bölümler ve Kategoriler
        sections_data = [
            {
                'title': 'Yazılımlar ve Araçlar',
                'order': 1,
                'categories': [
                    ('SPSS', 'spss', 'bi-bar-chart-fill'),
                    ('Python', 'python', 'bi-filetype-py'),
                    ('R', 'r-programlama', 'bi-code-slash'),
                    ('Excel', 'excel', 'bi-file-earmark-excel'),
                ]
            },
            {
                'title': 'Analiz Yöntemleri',
                'order': 2,
                'categories': [
                    ('İstatistik Temelleri', 'istatistik-temelleri', 'bi-calculator'),
                    ('Regresyon Analizi', 'regresyon', 'bi-graph-up'),
                    ('Faktör Analizi', 'faktor-analizi', 'bi-diagram-3'),
                    ('Yapısal Eşitlik', 'sem', 'bi-bezier2'),
                ]
            },
            {
                'title': 'Akademik Danışma',
                'order': 3,
                'categories': [
                    ('Tez Yazımı', 'tez-yazimi', 'bi-journal-text'),
                    ('Makale Yayınlama', 'makale', 'bi-newspaper'),
                    ('Araştırma Metodolojisi', 'metodoloji', 'bi-search'),
                    ('Akademik Kariyer', 'kariyer', 'bi-mortarboard'),
                ]
            },
        ]

        for section_data in sections_data:
            section, _ = Section.objects.get_or_create(
                title=section_data['title'],
                defaults={'order': section_data['order']}
            )
            for cat_title, cat_slug, cat_icon in section_data['categories']:
                Category.objects.get_or_create(
                    slug=cat_slug,
                    defaults={
                        'section': section,
                        'title': cat_title,
                        'icon_class': cat_icon
                    }
                )
        self.stdout.write(self.style.SUCCESS('Bölümler ve kategoriler oluşturuldu'))

        # 4. Örnek Konular ve Yanıtlar
        topics_data = [
            {
                'category_slug': 'spss',
                'subject': 'SPSS\'te Faktör Analizi Nasıl Yapılır?',
                'starter': expert_users[4],  # SPSSUzmani
                'content': '''Merhaba arkadaşlar,

Faktör analizi yapmak istiyorum ama adımları tam bilmiyorum.

Elimde 30 soruluk bir ölçek var ve bunları faktörlere ayırmam gerekiyor.

- KMO değeri ne olmalı?
- Varimax mı Oblimin mi kullanmalıyım?
- Faktör sayısına nasıl karar vereceğim?

Yardımcı olabilir misiniz?''',
                'replies': [
                    (expert_users[0], '''Faktör analizi için şu adımları takip edebilirsin:

1. **KMO ve Bartlett Testi**: Analyze > Dimension Reduction > Factor
   - KMO > 0.70 olmalı (ideal: >0.80)
   - Bartlett p < 0.05 olmalı

2. **Faktör Çıkarma**: Principal Component Analysis
   - Eigenvalue > 1 kuralı
   - Scree Plot'a bak

3. **Rotasyon**:
   - Faktörler ilişkisiz ise: Varimax
   - Faktörler ilişkili ise: Direct Oblimin

4. **Faktör Yükleri**:
   - 0.40 üzeri kabul edilebilir
   - Çapraz yüklenme varsa maddeyi çıkar

Başarılar!'''),
                ]
            },
            {
                'category_slug': 'python',
                'subject': 'Pandas ile Veri Temizleme Rehberi',
                'starter': expert_users[1],  # PythonGurusu
                'content': '''Python Pandas ile veri temizleme için temel adımlar:

```python
import pandas as pd

# Veri yükleme
df = pd.read_csv('veri.csv')

# Eksik değerleri kontrol et
df.isnull().sum()

# Eksik değerleri doldur
df.fillna(df.mean(), inplace=True)

# Duplike satırları sil
df.drop_duplicates(inplace=True)

# Veri tiplerini kontrol et
df.dtypes
```

Sorularınız varsa yazın!''',
                'replies': [
                    (expert_users[2], 'Çok faydalı bir özet olmuş. Outlier tespiti için de `df.describe()` ve box plot kullanılabilir.'),
                ]
            },
            {
                'category_slug': 'istatistik-temelleri',
                'subject': 'Hangi İstatistik Testini Kullanmalıyım?',
                'starter': expert_users[0],  # Dr_Mehmet_Stats
                'content': '''İstatistik testi seçimi için karar ağacı:

**Karşılaştırma yapıyorsan:**
- 2 grup, normal dağılım ✓ → Independent t-test
- 2 grup, normal dağılım ✗ → Mann-Whitney U
- 3+ grup, normal dağılım ✓ → ANOVA
- 3+ grup, normal dağılım ✗ → Kruskal-Wallis

**İlişki arıyorsan:**
- İki sürekli değişken, normal ✓ → Pearson Korelasyon
- İki sürekli değişken, normal ✗ → Spearman Korelasyon
- Kategorik değişkenler → Ki-Kare

**Tahmin yapıyorsan:**
- Sürekli bağımlı değişken → Regresyon
- Kategorik bağımlı değişken → Lojistik Regresyon

Sorularınızı bekliyorum!''',
                'replies': []
            },
            {
                'category_slug': 'tez-yazimi',
                'subject': 'Tez Yazarken En Çok Yapılan 5 Hata',
                'starter': expert_users[3],  # TezDanismani_Prof
                'content': '''Yıllardır tez danışmanlığı yapıyorum. En sık gördüğüm hatalar:

1. **Araştırma sorusu belirsiz**: Net ve ölçülebilir olmalı
2. **Literatür yetersiz**: En az 50-100 kaynak tarayın
3. **Metodoloji zayıf**: Neden bu yöntemi seçtiğinizi açıklayın
4. **Bulgular yorum içeriyor**: Bulgular objektif, yorumlar tartışmada
5. **APA/Kaynak hatası**: Referans yöneticisi kullanın (Zotero, Mendeley)

Sorularınız varsa çekinmeden sorun!''',
                'replies': [
                    (expert_users[0], 'Harika bir özet hocam! Özellikle 4. madde çok kritik. Bulgular kısmında "görüldüğü gibi" yerine sadece sayıları verin.'),
                    (expert_users[1], 'Zotero kullanımı için de bir rehber paylaşabilir misiniz?'),
                ]
            },
            {
                'category_slug': 'r-programlama',
                'subject': 'R ile Görselleştirme - ggplot2 Temelleri',
                'starter': expert_users[2],  # R_Uzmani
                'content': '''ggplot2 ile temel grafikler:

```r
library(ggplot2)

# Scatter plot
ggplot(data, aes(x=var1, y=var2)) +
  geom_point() +
  theme_minimal()

# Bar chart
ggplot(data, aes(x=kategori, fill=kategori)) +
  geom_bar() +
  labs(title="Dağılım")

# Histogram
ggplot(data, aes(x=skor)) +
  geom_histogram(bins=30, fill="steelblue")
```

Grafik örnekleri için sorabilirsiniz!''',
                'replies': []
            },
        ]

        for topic_data in topics_data:
            category = Category.objects.get(slug=topic_data['category_slug'])
            topic, created = Topic.objects.get_or_create(
                subject=topic_data['subject'],
                defaults={
                    'category': category,
                    'starter': topic_data['starter'],
                    'views': 100 + hash(topic_data['subject']) % 500
                }
            )
            if created:
                # İlk post (konu içeriği)
                Post.objects.create(
                    topic=topic,
                    message=topic_data['content'],
                    created_by=topic_data['starter']
                )
                # Yanıtlar
                for replier, reply_content in topic_data['replies']:
                    Post.objects.create(
                        topic=topic,
                        message=reply_content,
                        created_by=replier
                    )
        self.stdout.write(self.style.SUCCESS(f'{len(topics_data)} konu oluşturuldu'))

        # 5. Günün İpucu
        tips_data = [
            {
                'title': 'SPSS\'te Missing Value Kodlaması',
                'content': '''Eksik değerleri kodlamak için:

Transform > Recode into Different Variables

• 99, 999 gibi değerleri System Missing yapın
• Analiz sonuçlarını etkilemesinler
• Recode işlemi orijinal değişkeni korur

💡 İpucu: Orijinal veriyi her zaman yedekleyin!''',
                'category': 'spss',
                'publish_date': timezone.now().date(),
            },
        ]

        for tip_data in tips_data:
            DailyTip.objects.get_or_create(
                title=tip_data['title'],
                defaults={
                    'content': tip_data['content'],
                    'category': tip_data['category'],
                    'publish_date': tip_data['publish_date'],
                    'is_active': True,
                    'created_by': admin
                }
            )
        self.stdout.write(self.style.SUCCESS('Günün ipucu oluşturuldu'))

        # 6. Quiz Soruları
        questions = [
            {
                'question': 'Hangi test için normal dağılım varsayımı GEREKLİ DEĞİLDİR?',
                'option_a': 'Independent t-test',
                'option_b': 'Mann-Whitney U',
                'option_c': 'Pearson Korelasyon',
                'option_d': 'ANOVA',
                'correct_answer': 'B',
                'category': 'statistics',
                'difficulty': 'medium',
            },
            {
                'question': 'SPSS\'de veri dosyası hangi uzantıyla kaydedilir?',
                'option_a': '.xlsx',
                'option_b': '.csv',
                'option_c': '.sav',
                'option_d': '.spv',
                'correct_answer': 'C',
                'category': 'spss',
                'difficulty': 'easy',
            },
            {
                'question': 'Python\'da pandas ile eksik değerler nasıl kontrol edilir?',
                'option_a': 'df.empty()',
                'option_b': 'df.isnull()',
                'option_c': 'df.missing()',
                'option_d': 'df.blank()',
                'correct_answer': 'B',
                'category': 'python',
                'difficulty': 'easy',
            },
            {
                'question': 'Cronbach Alpha değeri kaçın üzerinde olmalıdır?',
                'option_a': '0.50',
                'option_b': '0.60',
                'option_c': '0.70',
                'option_d': '0.90',
                'correct_answer': 'C',
                'category': 'statistics',
                'difficulty': 'medium',
            },
            {
                'question': 'R\'da veri çerçevesi oluşturmak için hangi fonksiyon kullanılır?',
                'option_a': 'create.frame()',
                'option_b': 'data.frame()',
                'option_c': 'make.df()',
                'option_d': 'new.data()',
                'correct_answer': 'B',
                'category': 'r',
                'difficulty': 'easy',
            },
        ]

        for q in questions:
            QuizQuestion.objects.get_or_create(
                question=q['question'],
                defaults=q
            )
        self.stdout.write(self.style.SUCCESS(f'{len(questions)} quiz sorusu oluşturuldu'))

        self.stdout.write(self.style.SUCCESS('✅ Tüm örnek veriler yüklendi!'))
