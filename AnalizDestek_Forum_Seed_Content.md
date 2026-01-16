# 📊 FORUM SEED CONTENT PAKETİ - BÖLÜM 1
## AnalizDestek Forum İçerik Tohumlaması

---

# KATEGORİ 1: YAZILIMLAR VE ARAÇLAR > SPSS (15 Soru)

## SORU 1: Normallik Testi Yorumlama ✅ ÇÖZÜLDÜ
**Başlık:** SPSS'te normallik testi sonuçlarını nasıl yorumlarım?
**Kullanıcı:** YeniAraştırmacı23 | **Tarih:** 10 Ocak 2026 | **Görüntülenme:** 234
**Etiketler:** #SPSS #NormallikTesti #Varsayımlar

Merhaba arkadaşlar, lisans tezim için 150 kişiden veri topladım. SPSS'te normallik testi yaptım ama Kolmogorov-Smirnov ve Shapiro-Wilk'den hangisine bakmalıyım? p değeri 0.05'ten küçük, bu ne anlama geliyor?

**✅ EN FAYDA YANIT** (Dr_Mehmet_Stats - 18 beğeni):
Örneklem 150 olduğu için Kolmogorov-Smirnov'a bak. p<0.05 ise veriler normal dağılmıyor ama örneklem büyüklüğün 150 olduğu için merkezi limit teoremi devreye girer. Histogram ve Q-Q Plot'a da mutlaka bak!

---

## SORU 2: T-Testi mi ANOVA mı?
**Başlık:** İki gruptan fazlası için T-testi yapılır mı?
**Kullanıcı:** TezYolculugu2024 | **Tarih:** 12 Ocak 2026 | **Görüntülenme:** 156
**Etiketler:** #SPSS #T-Test #ANOVA #FarkTestleri

3 farklı eğitim seviyesi var (lise, üniversite, yüksek lisans). Hepsini birbirine t-testi ile karşılaştırsam olur mu?

**✅ EN FAYDA YANIT** (Dr_Mehmet_Stats - 22 beğeni):
HAYIR! Çok önemli bir hata yapmak üzeresin. T-Testi sadece 2 grup için. 3+ grup için ANOVA kullanmalısın. Her ikiliyi ayrı t-testi yaparsan Tip I hata riski artar. ANOVA sonrası Post-Hoc (Tukey HSD) yap.

---

## SORU 3: Cronbach Alpha Düşük ✅ ÇÖZÜLDÜ
**Başlık:** Cronbach Alpha 0.68 kabul edilir mi?
**Kullanıcı:** AnketUstasi | **Tarih:** 13 Ocak 2026 | **Görüntülenme:** 412
**Etiketler:** #SPSS #Güvenilirlik #CronbachAlpha

8 maddelik ölçekte Cronbach Alpha = 0.685 çıktı. Tez jürisinde kabul eder mi?

**✅ EN FAYDA YANIT** (Dr_Mehmet_Stats - 25 beğeni):
0.68 "kabul edilebilir" sınırda. α ≥ 0.70 ideal ama yeni ölçekler için 0.60-0.70 geçilebilir. Item-Total Statistics tablosuna bak, "Cronbach's Alpha if Item Deleted" sütununda alpha'yı düşüren maddeyi çıkarmayı değerlendir.

---

## SORU 4: Regresyon R² Değeri
**Başlık:** R Square 0.15 çok düşük mü?
**Kullanıcı:** SosyalBilimci | **Tarih:** 14 Ocak 2026 | **Görüntülenme:** 289
**Etiketler:** #SPSS #Regresyon #RSquare

R² = 0.154 çıktı. Bu çok düşük değil mi?

**✅ EN FAYDA YANIT** (Dr_Mehmet_Stats - 20 beğeni):
Sosyal bilimlerde R²=0.15 orta etki büyüklüğü. İş tatmini gibi karmaşık değişkenleri açıklamak zor, %15 kötü değil. ANOVA tablosunda model anlamlıysa (p<0.05) savunabilirsin.

---

## SORU 5: Veri Kodlama ✅ ÇÖZÜLDÜ
**Başlık:** SPSS'te 5'li Likert verileri nasıl girilir?
**Kullanıcı:** YeniBaslayan2024 | **Tarih:** 9 Ocak 2026 | **Görüntülenme:** 178
**Etiketler:** #SPSS #VeriGirişi #Likert

"Kesinlikle Katılmıyorum" 1 mi 5 mi olmalı? Ters maddeler nasıl kodlanır?

**✅ EN FAYDA YANIT** (AnalizMeraklisi - 16 beğeni):
Standart kodlama: 1=Kesinlikle Katılmıyorum, 5=Kesinlikle Katılıyorum. Ters maddeler için: Transform > Compute Variable > 6 - [eski değer]. Yeni değişken adını S7_R gibi yap.

---

## SORU 6: Frekans Tablosu
**Başlık:** Frequencies'te "Valid Percent" vs "Percent"
**Kullanıcı:** AnketAnalisti | **Tarih:** 11 Ocak 2026 | **Görüntülenme:** 145
**Etiketler:** #SPSS #FrekansAnalizi

Hangisini rapor etmeliyim?

**✅ EN FAYDA YANIT** (Dr_Mehmet_Stats - 14 beğeni):
Valid Percent kullan! Eksik veriler hariç gerçek dağılımı gösterir. "Katılımcıların %55.2'si (n=99) kadın" gibi raporla.

---

## SORU 7: Correlation vs Regression ✅ ÇÖZÜLDÜ
**Başlık:** Korelasyon ve regresyon farkı nedir?
**Kullanıcı:** KavramKarmasasi | **Tarih:** 8 Ocak 2026 | **Görüntülenme:** 367
**Etiketler:** #Korelasyon #Regresyon

İkisi de ilişkiye bakıyor gibi, hangisi ne zaman kullanılır?

**✅ EN FAYDA YANIT** (Dr_Mehmet_Stats - 28 beğeni):
Korelasyon: "İlişki var mı?" (iki yönlü, r değeri)
Regresyon: "X, Y'yi yordayabilir mi?" (tek yönlü, R² ve tahmin denklemi)
Basit regresyonda r²=R². Çoklu yordayıcı varsa regresyon kullan.

---

## SORU 8: Outlier Tespiti ✅ ÇÖZÜLDÜ
**Başlık:** SPSS'te uç değerleri nasıl bulup temizlerim?
**Kullanıcı:** VeriTemizleyici | **Tarih:** 7 Ocak 2026 | **Görüntülenme:** 223
**Etiketler:** #SPSS #OutlierAnalizi

Danışmanım "uç değer analizi yap" dedi. Nasıl yapılır?

**✅ EN FAYDA YANIT** (Dr_Mehmet_Stats - 19 beğeni):
Analyze > Explore > Box Plot çiz. ⭕ ve ⭐ işaretli noktalar outlier. Z-Score kullan: |Z|>3.0 aşırı uç. Veri hatası değilse direkt silme! Log transformation veya winsorize dene.

---

## SORU 9: Missing Data
**Başlık:** Eksik verileri nasıl ele almalıyım?
**Kullanıcı:** KayipVeriKabusu | **Tarih:** 6 Ocak 2026 | **Görüntülenme:** 198
**Etiketler:** #SPSS #MissingData

%12 eksik veri var. Kabul edilebilir mi?

**✅ EN FAYDA YANIT** (Dr_Mehmet_Stats - 21 beğeni):
%12 yönetilebilir. Analyze > Missing Value Analysis yap. %5-15 arası için Mean Imputation veya Multiple Imputation kullan. Tez için en güvenli: Listwise deletion + raporunda belirt.

---

## SORU 10: Chi-Square Test ✅ ÇÖZÜLDÜ
**Başlık:** Ki-Kare testi ne zaman kullanılır?
**Kullanıcı:** KategorikKarmasik | **Tarih:** 5 Ocak 2026 | **Görüntülenme:** 267
**Etiketler:** #SPSS #ChiSquare #KategorikVeri

Cinsiyet × Meslek Memnuniyeti ilişkisi test edilir mi?

**✅ EN FAYDA YANIT** (Dr_Mehmet_Stats - 24 beğeni):
İki kategorik değişken → Chi-Square! Analyze > Crosstabs > Statistics: Chi-square işaretle. p<0.05 ise anlamlı ilişki var. Expected Count ≥ 5 olmalı, yoksa Fisher's Exact kullan.

# KATEGORİ 1 DEVAM: SPSS (Soru 11-15)

## SORU 11: Paired T-Test ✅ ÇÖZÜLDÜ
**Başlık:** Ön test - son test için hangi t-testi?
**Kullanıcı:** DeneyselDesen | **Tarih:** 4 Ocak 2026 | **Görüntülenme:** 312
**Etiketler:** #SPSS #PairedSamples #ÖnTestSonTest

Aynı kişilere önceden ve sonradan test uyguladım. Hangi t-testi?

**✅ EN FAYDA YANIT** (Dr_Mehmet_Stats - 26 beğeni):
Aynı kişi, iki ölçüm → Paired Samples T-Test! Analyze > Compare Means > Paired-Samples T Test. p<0.05 ise anlamlı fark var. Cohen's d hesapla: d = Mean Diff / SD.

---

## SORU 12: Scatterplot
**Başlık:** SPSS'te scatter plot nasıl çizilir?
**Kullanıcı:** GorselArayici | **Tarih:** 3 Ocak 2026 | **Görüntülenme:** 189
**Etiketler:** #SPSS #Scatterplot #Visualization

İki değişken ilişkisini görselleştirmek istiyorum.

**✅ EN FAYDA YANIT** (GrafikleriSeviyorum - 17 beğeni):
Graphs > Legacy Dialogs > Scatter/Dot > Simple. Y Axis: Bağımlı, X Axis: Bağımsız. Çift tıkla > Elements > Fit Line at Total > R² göster.

---

## SORU 13: ANOVA Post-Hoc ✅ ÇÖZÜLDÜ
**Başlık:** ANOVA anlamlı çıktı, şimdi ne yapmalıyım?
**Kullanıcı:** PostHocKarmasasi | **Tarih:** 2 Ocak 2026 | **Görüntülenme:** 278
**Etiketler:** #SPSS #ANOVA #PostHoc #TukeyHSD

Hangi gruplar farklı diye nasıl bulurum?

**✅ EN FAYDA YANIT** (Dr_Mehmet_Stats - 23 beğeni):
Post-Hoc Test gerek! Levene p>0.05 ise Tukey HSD, p<0.05 ise Games-Howell kullan. Analyze > One-Way ANOVA > Post Hoc. Multiple Comparisons tablosunda p<0.05 olanlar farklı.

---

## SORU 14: Likert Puanlama ✅ ÇÖZÜLDÜ
**Başlık:** Likert ölçekten toplam puan hesaplama
**Kullanıcı:** ÖlçekGelistirici | **Tarih:** 1 Ocak 2026 | **Görüntülenme:** 256
**Etiketler:** #SPSS #LikertÖlçek #ToplamPuan

10 maddelik stres ölçeği. Toplam puan nasıl hesaplanır?

**✅ EN FAYDA YANIT** (Dr_Mehmet_Stats - 19 beğeni):
Önce ters maddeleri düzelt (6 - eski değer). Sonra Transform > Compute > MEAN(S1,S2,...S10). MEAN kullan çünkü eksik veri olsa bile ortalama alır. MEAN.8 = en az 8 madde dolu olmalı.

---

## SORU 15: Mediation Analysis
**Başlık:** SPSS'te aracılık analizi nasıl yapılır?
**Kullanıcı:** AracılikMerakli | **Tarih:** 15 Aralık 2025 | **Görüntülenme:** 402
**Etiketler:** #SPSS #Mediation #Hayes #PROCESS

Liderlik → Motivasyon → Performans modeli test etmek istiyorum.

**✅ EN FAYDA YANIT** (Dr_Mehmet_Stats - 31 beğeni):
Andrew Hayes'in PROCESS Macro kullan! processmacro.org'dan indir. Model 4 (simple mediation) seç. Bootstrap 5000 ile test et. LLCI-ULCI 0'ı içermiyorsa anlamlı aracılık var.

---

# KATEGORİ 2: PYTHON & R (10 Soru)

## SORU 16: Python Veri Okuma ✅ ÇÖZÜLDÜ
**Başlık:** Pandas ile Excel dosyası nasıl okunur?
**Kullanıcı:** PythonYolcusu | **Tarih:** 14 Ocak 2026 | **Görüntülenme:** 289
**Etiketler:** #Python #Pandas #ExcelOkuma

FileNotFoundError hatası alıyorum!

**✅ EN FAYDA YANIT** (PythonGurusu - 22 beğeni):
```python
import pandas as pd
df = pd.read_excel(r'C:\Users\...\veri.xlsx')  # Raw string kullan
print(df.head())
```
openpyxl yok ise: `pip install openpyxl`

---

## SORU 17: Python Descriptives
**Başlık:** Pandas ile temel istatistikler
**Kullanıcı:** İstatistikPython | **Tarih:** 13 Ocak 2026 | **Görüntülenme:** 245
**Etiketler:** #Python #Pandas #Tanımlayıcı

SPSS Descriptives gibi çıktı alabilir miyim?

**✅ EN FAYDA YANIT** (PythonGurusu - 24 beğeni):
```python
print(df.describe())  # Özet istatistik
print(df['Yas'].mean())  # Ortalama
print(df['Yas'].std())   # Std sapma
print(df['Yas'].skew())  # Çarpıklık
```

---

## SORU 18: R T-Test ✅ ÇÖZÜLDÜ
**Başlık:** R'da independent t-test nasıl yapılır?
**Kullanıcı:** RYolculugu | **Tarih:** 12 Ocak 2026 | **Görüntülenme:** 198
**Etiketler:** #RStudio #T-Test

R Studio'da iki grup arası t-testi yapmak istiyorum.

**✅ EN FAYDA YANIT** (R_Uzmani - 20 beğeni):
```r
data <- read.csv("veri.csv")
t_test <- t.test(Puan ~ Cinsiyet, data=data, var.equal=TRUE)
print(t_test)
# p<0.05 ise anlamlı fark var
```

---

## SORU 19: Python Correlation Heatmap ✅ ÇÖZÜLDÜ
**Başlık:** Python ile korelasyon matrisi ve heatmap
**Kullanıcı:** MatrisArayıcı | **Tarih:** 11 Ocak 2026 | **Görüntülenme:** 312
**Etiketler:** #Python #Korelasyon #Heatmap #Seaborn

Birden fazla değişken arası korelasyon görmek istiyorum.

**✅ EN FAYDA YANIT** (PythonGurusu - 26 beğeni):
```python
import seaborn as sns
import matplotlib.pyplot as plt
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.show()
```

---

## SORU 20: R ANOVA Visualization
**Başlık:** R'da ANOVA sonuçlarını görselleştirme
**Kullanıcı:** RGorsellestirici | **Tarih:** 10 Ocak 2026 | **Görüntülenme:** 176
**Etiketler:** #RStudio #ANOVA #ggplot2

ANOVA sonuçlarını bar chart ile göstermek istiyorum.

**✅ EN FAYDA YANIT** (R_Uzmani - 19 beğeni):
```r
library(ggplot2)
anova_model <- aov(Puan ~ EgitimSeviyesi, data=data)
ggplot(data, aes(x=EgitimSeviyesi, y=Puan, fill=EgitimSeviyesi)) +
  geom_boxplot() + theme_minimal()
```

---

## SORU 21: Python Regression ✅ ÇÖZÜLDÜ
**Başlık:** Python'da basit doğrusal regresyon
**Kullanıcı:** RegressionSeeker | **Tarih:** 9 Ocak 2026 | **Görüntülenme:** 234
**Etiketler:** #Python #Regression #sklearn

Çalışma saati ile sınav notu arasında regresyon yapmak istiyorum.

**✅ EN FAYDA YANIT** (PythonGurusu - 21 beğeni):
```python
from sklearn.linear_model import LinearRegression
import numpy as np
X = df[['CalismaS aati']].values
y = df['SinavNotu'].values
model = LinearRegression()
model.fit(X, y)
print(f'R² = {model.score(X, y):.3f}')
print(f'Eğim = {model.coef_[0]:.2f}')
```

---

## SORU 22: R Data Cleaning
**Başlık:** R'da eksik verileri temizleme
**Kullanıcı:** DataCleanerR | **Tarih:** 8 Ocak 2026 | **Görüntülenme:** 167
**Etiketler:** #RStudio #DataCleaning #MissingData

R'da NA değerleri nasıl yönetirim?

**✅ EN FAYDA YANIT** (R_Uzmani - 18 beğeni):
```r
# NA'ları görüntüle
sum(is.na(data))
colSums(is.na(data))

# NA'ları çıkar (listwise)
data_clean <- na.omit(data)

# NA'ları ortalama ile doldur
data$Yas[is.na(data$Yas)] <- mean(data$Yas, na.rm=TRUE)
```

---

## SORU 23: Python Chi-Square
**Başlık:** Python'da Ki-Kare testi
**Kullanıcı:** ChiSquarePython | **Tarih:** 7 Ocak 2026 | **Görüntülenme:** 198
**Etiketler:** #Python #ChiSquare #Scipy

İki kategorik değişken arası ilişki test etmek istiyorum.

**✅ EN FAYDA YANIT** (PythonGurusu - 20 beğeni):
```python
from scipy.stats import chi2_contingency
import pandas as pd
crosstab = pd.crosstab(df['Cinsiyet'], df['Meslek'])
chi2, p, dof, expected = chi2_contingency(crosstab)
print(f'Chi2={chi2:.2f}, p={p:.4f}')
# p<0.05 ise anlamlı ilişki var
```

---

## SORU 24: R Hypothesis Testing
**Başlık:** R'da normallik testi
**Kullanıcı:** NormalityTest | **Tarih:** 6 Ocak 2026 | **Görüntülenme:** 189
**Etiketler:** #RStudio #NormalityTest #ShapiroWilk

Veri normal dağılıyor mu test etmek istiyorum.

**✅ EN FAYDA YANIT** (R_Uzmani - 17 beğeni):
```r
# Shapiro-Wilk testi
shapiro.test(data$Puan)
# p>0.05 ise normal dağılıyor

# Görsel
hist(data$Puan, main="Histogram")
qqnorm(data$Puan)
qqline(data$Puan, col="red")
```

---

## SORU 25: Python Time Series
**Başlık:** Python'da zaman serisi analizi
**Kullanıcı:** TimeSeriesAnalyst | **Tarih:** 5 Ocak 2026 | **Görüntülenme:** 212
**Etiketler:** #Python #TimeSeries #Pandas

Tarih bazlı verileri nasıl analiz ederim?

**✅ EN FAYDA YANIT** (PythonGurusu - 19 beğeni):
```python
import pandas as pd
df['Tarih'] = pd.to_datetime(df['Tarih'])
df.set_index('Tarih', inplace=True)
df_monthly = df.resample('M').mean()  # Aylık ortalama
df.plot(figsize=(12,6))
```

# KATEGORİ 3: ANALİZ YÖNTEMLERİ (10 Soru)

## SORU 26: Faktör Analizi ✅ ÇÖZÜLDÜ
**Başlık:** SPSS'te faktör analizi nasıl yorumlanır?
**Kullanıcı:** FaktorAvcisi | **Tarih:** 4 Ocak 2026 | **Görüntülenme:** 345
**Etiketler:** #SPSS #FaktorAnalizi #KMO #ÖlçekGeliştirme

Ölçeğimin kaç boyutlu olduğunu bulmak istiyorum. KMO ve Bartlett testleri nedir?

**✅ EN FAYDA YANIT** (Dr_Mehmet_Stats - 29 beğeni):
Analyze > Dimension Reduction > Factor. 
**KMO ≥ 0.60** olmalı (tercihan 0.80+). **Bartlett p<0.05** olmalı.
Total Variance Explained'de Eigenvalue >1 olanlar faktör sayısı. Rotated Component Matrix'te yükleme ≥0.40 olanlar o faktöre ait.

---

## SORU 27: Örneklem Büyüklüğü
**Başlık:** Tez için kaç kişiye anket uygulamalıyım?
**Kullanıcı:** OrneklemKararsizi | **Tarih:** 3 Ocak 2026 | **Görüntülenme:** 567
**Etiketler:** #Örneklem #AnketTasarımı #GüçAnalizi

250 kişi yeterli mi yoksa daha fazla mı gerekli?

**✅ EN FAYDA YANIT** (MetodologiUzmani - 33 beğeni):
**Minimum kurallar:**
- Tanımlayıcı araştırma: n≥100
- Korelasyon: n≥30 (tercihan 50+)
- t-test/ANOVA: Her grupta n≥30
- Regresyon: 10-15 kişi × değişken sayısı
- Faktör analizi: 5-10 kişi × madde sayısı, min. 150
250 genel araştırmalar için yeterli. G*Power ile güç analizi yap!

---

## SORU 28: SEM (Yapısal Eşitlik) ✅ ÇÖZÜLDÜ
**Başlık:** AMOS ile SEM analizi nasıl yapılır?
**Kullanıcı:** SEMYolculugu | **Tarih:** 2 Ocak 2026 | **Görüntülenme:** 423
**Etiketler:** #AMOS #SEM #YapısalEşitlik #ModelUyumu

Model uyum indekslerini nasıl yorumlarım?

**✅ EN FAYDA YANIT** (SEM_Uzmani - 27 beğeni):
**Model Fit İndeksleri:**
- **χ²/df < 5** (ideal <3)
- **CFI ≥ 0.90** (ideal ≥0.95)
- **TLI ≥ 0.90**
- **RMSEA < 0.08** (ideal <0.06)
- **SRMR < 0.08**
Hepsinin aynı anda mükemmel olması gerekmez. 3-4 indeks kabul edilebilir değerlerde ise model uyumludur.

---

## SORU 29: Güvenilirlik vs Geçerlilik
**Başlık:** Güvenilirlik ve geçerlilik farkı nedir?
**Kullanıcı:** KavramNetligi | **Tarih:** 1 Ocak 2026 | **Görüntülenme:** 289
**Etiketler:** #Güvenilirlik #Geçerlilik #ÖlçekGeliştirme

İkisi arasındaki farkı anlamıyorum!

**✅ EN FAYDA YANIT** (Dr_Mehmet_Stats - 25 beğeni):
**Güvenilirlik (Reliability):** Ölçüm tutarlılığı. "Aynı şeyi tekrar ölçsem aynı sonucu alır mıyım?"
Test: Cronbach Alpha, test-retest

**Geçerlilik (Validity):** Ölçmek istediğini ölçüyor mu? "Stres ölçeği gerçekten stresi mi ölçüyor?"
Test: Faktör analizi, criterion validity

Önce GÜVENİLİR olmalı, sonra GEÇERLİ olabilir!

---

## SORU 30: Moderation (Düzenleyicilik)
**Başlık:** Moderatör etki nasıl test edilir?
**Kullanıcı:** ModeratorArayan | **Tarih:** 30 Aralık 2025 | **Görüntülenme:** 312
**Etiketler:** #Moderation #PROCESS #Hayes #Etkileşim

Yaş, liderlik-performans ilişkisini düzenliyor mu test etmek istiyorum.

**✅ EN FAYDA YANIT** (Dr_Mehmet_Stats - 24 beğeni):
PROCESS Macro Model 1 kullan!
```
X = Liderlik
Y = Performans
W = Yaş (moderator)
```
Etkileşim terimi (X×W) anlamlıysa moderasyon var. Conditional effects tablosunda farklı yaş gruplarında etkiyi gör.

---

## SORU 31: Meta-Analiz
**Başlık:** Meta-analiz nedir ve nasıl yapılır?
**Kullanıcı:** MetaAnalist | **Tarih:** 29 Aralık 2025 | **Görüntülenme:** 198
**Etiketler:** #Meta-Analiz #EffectSize #CMA

Birçok çalışmayı birleştirerek analiz yapmak istiyorum.

**✅ EN FAYDA YANIT** (MetodologiUzmani - 22 beğeni):
Meta-analiz = çalışmaların etki büyüklüklerini birleştirme. CMA (Comprehensive Meta-Analysis) yazılımı kullan. Her çalışmadan effect size (Cohen's d, r, OR) hesapla. Forest plot çiz. Heterogeneity (I²) kontrol et. I²>75% ise random-effects model kullan.

---

## SORU 32: Ölçek Uyarlama ✅ ÇÖZÜLDÜ
**Başlık:** Yabancı ölçeği Türkçe'ye uyarlama adımları
**Kullanıcı:** OlcekUyarlayici | **Tarih:** 28 Aralık 2025 | **Görüntülenme:** 434
**Etiketler:** #ÖlçekUyarlama #Çeviri #Geçerlilik

İngilizce bir ölçeği Türkçe'ye uyarlamak istiyorum. Nasıl yapmalıyım?

**✅ EN FAYDA YANIT** (TezDanismani_Prof - 30 beğeni):
**Adımlar:**
1. **İzin al** (orijinal yazardan email)
2. **Çeviri-Geri Çeviri:** 2 uzman çevirir, 2 uzman geri çevirir
3. **Uzman görüşü:** 5-7 uzman kapsam geçerliliği değerlendirir (CVI)
4. **Pilot uygulama:** 50 kişi
5. **Ana uygulama:** 200+ kişi
6. **Güvenilirlik:** Cronbach Alpha ≥0.70
7. **Yapı geçerliliği:** DFA (Doğrulayıcı Faktör Analizi)

---

## SORU 33: Anket Tasarımı
**Başlık:** Anket soruları nasıl yazılmalı?
**Kullanıcı:** AnketYazari | **Tarih:** 27 Aralık 2025 | **Görüntülenme:** 378
**Etiketler:** #AnketTasarımı #SoruYazımı #LikertÖlçek

İlk defa anket hazırlıyorum. Nelere dikkat etmeliyim?

**✅ EN FAYDA YANIT** (AnketUzmani - 26 beğeni):
**İyi Anket Kuralları:**
✅ Kısa ve öz cümleler
✅ Tek bir şey soran sorular (çift yüklü soru YOK)
✅ Yönlendirici ifade kullanma
✅ Akademik dil yerine günlük dil
✅ 5'li Likert ideal (3'lü dar, 7'li karmaşık)
❌ "değil mi, gibi" ifadeleri kullanma
❌ Negatif cümle + ters kodlama = karışıklık

**Örnek Kötü:** "İşinizden memnun değil misiniz ve işten ayrılmayı düşünmüyor musunuz?"
**İyi:** "İşimden memnunum" (1-5 Likert)

---

## SORU 34: Non-Parametrik Testler
**Başlık:** Parametrik vs non-parametrik test farkı
**Kullanıcı:** TestSecici | **Tarih:** 26 Aralık 2025 | **Görüntülenme:** 267
**Etiketler:** #NonParametrik #MannWhitney #KruskalWallis

Normal dağılım yok, hangi testi kullanmalıyım?

**✅ EN FAYDA YANIT** (Dr_Mehmet_Stats - 23 beğeni):
**Parametrik → Non-Parametrik:**
- Independent t-test → **Mann-Whitney U**
- Paired t-test → **Wilcoxon Signed-Rank**
- One-Way ANOVA → **Kruskal-Wallis H**
- Pearson r → **Spearman rho**

Non-parametrik testler dağılım varsayımı gerektirmez ama güç kaybı yaşatır. Örneklem >30 ve hafif sapma varsa parametrik kullanabilirsin (merkezi limit teoremi).

---

## SORU 35: Effect Size (Etki Büyüklüğü) ✅ ÇÖZÜLDÜ
**Başlık:** Etki büyüklüğü nedir ve neden önemli?
**Kullanıcı:** EtkiBuyuklugu | **Tarih:** 25 Aralık 2025 | **Görüntülenme:** 298
**Etiketler:** #EffectSize #CohenD #EtaBuKaresi

p değeri anlamlı ama jüri "etki büyüklüğü" soruyor!

**✅ EN FAYDA YANIT** (MetodologiUzmani - 28 beğeni):
**p-değeri:** Anlamlılık (rastgele mi?)
**Effect size:** Etkinin büyüklüğü (pratikte önemli mi?)

**Cohen's d (t-test için):**
- d = 0.20 → Küçük
- d = 0.50 → Orta
- d = 0.80 → Büyük

**Eta-squared (ANOVA için):**
- η² = 0.01 → Küçük
- η² = 0.06 → Orta
- η² = 0.14 → Büyük

**R² (Regresyon):** Açıklanan varyans

Raporda her zaman effect size belirt! APA 7 zorunlu kıldı.

---

# KATEGORİ 4: AKADEMİK DANIŞMA (10 Soru)

## SORU 36: Tez Konusu Seçimi
**Başlık:** Tez konumu nasıl belirlemeliyim?
**Kullanıcı:** TezBaslangici | **Tarih:** 24 Aralık 2025 | **Görüntülenme:** 512
**Etiketler:** #TezKonusu #AraştırmaProblemi #Literatür

Tez konusu bulamıyorum, nereden başlamalıyım?

**✅ EN FAYDA YANIT** (TezDanismani_Prof - 35 beğeni):
**Adımlar:**
1. **İlgi alanını belirle** (hangi dersler keyifli geldi?)
2. **Son 5 yıl literatür tara:** Web of Science, Google Scholar
3. **Gap (boşluk) bul:** "Bu konuda şu araştırılmamış"
4. **Uygulanabilir olmalı:** Veriye erişim var mı? Süre yeterli mi?
5. **Danışmanla uyum:** Danışmanın uzmanlık alanına yakın olmalı

**Kırmızı bayraklar:**
❌ Çok geniş konu: "Türkiye'de eğitim sistemi"
❌ Veri toplama zor: "CEO'ların kişilik özellikleri"
❌ Güncel değil: 10+ yıl önceki trend

---

## SORU 37: Literatür Taraması ✅ ÇÖZÜLDÜ
**Başlık:** Literatür taraması nasıl yapılır?
**Kullanıcı:** LiteraturAvcisi | **Tarih:** 23 Aralık 2025 | **Görüntülenme:** 445
**Etiketler:** #LiteratürTaraması #MakaleArama #Kaynak

Hangi veritabanlarını kullanmalıyım? Kaç makale okumam gerekli?

**✅ EN FAYDA YANIT** (AkademikYazim - 31 beğeni):
**Veritabanları:**
1. **Web of Science** (en prestijli)
2. **Scopus**
3. **Google Scholar** (geniş ama düşük kalite olabilir)
4. **PubMed** (sağlık bilimleri)
5. **ERIC** (eğitim)

**Strateji:**
- **Son 5-10 yıl** odaklan (eskiler sadece teorik çerçeve için)
- **Review article** bul (özet çalışmalar)
- **Atıf takibi:** İyi makaleye kim atıf yapmış?
- **Snowballing:** Kaynakçadan geri git

**Kaç makale?**
- Lisans: 30-50
- Y. Lisans: 50-100
- Doktora: 150+

**Organize et:** Mendeley, Zotero, EndNote

---

## SORU 38: Metodoloji Bölümü
**Başlık:** Tez metodoloji bölümü nasıl yazılır?
**Kullanıcı:** MetodYazari | **Tarih:** 22 Aralık 2025 | **Görüntülenme:** 389
**Etiketler:** #Metodoloji #TezYazımı #AraştırmaDeseni

Metodolojide ne yazmalıyım? Neleri dahil etmeliyim?

**✅ EN FAYDA YANIT** (TezDanismani_Prof - 29 beğeni):
**Metodoloji Alt Başlıkları:**

**3.1. Araştırma Modeli/Deseni**
- Nicel/Nitel/Karma
- Tarama/İlişkisel/Deneysel

**3.2. Evren ve Örneklem**
- Evren: Kim? (ör: Ankara'daki lise öğrencileri)
- Örnekleme yöntemi: Rastgele/Uygun/Kar topu
- Örneklem büyüklüğü: N=250

**3.3. Veri Toplama Araçları**
- Kullanılan ölçekler
- Geçerlilik-güvenilirlik değerleri
- Kaç madde? Kaç boyut?

**3.4. Verilerin Toplanması**
- Nasıl uygulandı? (online/yüz yüze)
- Ne kadar sürede?
- Etik kurul var mı?

**3.5. Verilerin Analizi**
- Hangi programlar? (SPSS 28.0)
- Hangi testler? (t-test, ANOVA, regresyon)
- Anlamlılık düzeyi: α=0.05

---

## SORU 39: Etik Kurul Başvurusu
**Başlık:** Etik kurul onayı nasıl alınır?
**Kullanıcı:** EtikBasvuran | **Tarih:** 21 Aralık 2025 | **Görüntülenme:** 356
**Etiketler:** #EtikKurul #EtikOnay #Anket

Anket uygulamak için etik kurul şart mı? Nasıl başvurulur?

**✅ EN FAYDA YANIT** (AkademikSurecler - 27 beğeni):
**2020 sonrası TÜM araştırmalar etik kurul gerektirir!**

**Başvuru Adımları:**
1. **Üniversitenin etik kurul sistemine gir** (genelde EBYS)
2. **Gerekli belgeler:**
   - Araştırma önerisi
   - Anket/ölçek örnekleri
   - Bilgilendirilmiş onam formu
   - Danışman onay belgesi
3. **Ücret öde** (genelde 200-500 TL)
4. **Kurul toplantısını bekle** (ayda 1 kez)
5. **Onay gelirse veri toplamaya başla**

**Süre:** 2-4 hafta
**Not:** Etik onay OLMADAN veri toplama = tez kabul edilmez!

---

## SORU 40: Makale Yazımı (APA 7) ✅ ÇÖZÜLDÜ
**Başlık:** APA 7 formatında kaynak gösterme
**Kullanıcı:** APAKarmasasi | **Tarih:** 20 Aralık 2025 | **Görüntülenme:** 478
**Etiketler:** #APA7 #Kaynak #MakaleYazımı

Metin içi atıf ve kaynakça nasıl yazılır?

**✅ EN FAYDA YANIT** (AkademikYazim - 32 beğeni):
**Metin İçi Atıf:**
```
Tek yazar: (Smith, 2020)
İki yazar: (Smith & Jones, 2020)
3+ yazar: (Smith et al., 2020)
Birden fazla: (Smith, 2019; Jones, 2020)
Doğrudan alıntı: (Smith, 2020, p. 15)
```

**Kaynakça:**
```
Makale:
Smith, J., & Jones, M. (2020). Başlık burada. Journal Name, 15(3), 123-145. 
https://doi.org/10.xxxx

Kitap:
Smith, J. (2020). Kitap başlığı (2. baskı). Yayınevi.

Web:
Smith, J. (2020, Ocak 15). Başlık. Site Adı. https://www.site.com
```

**NOT:** DOI varsa mutlaka ekle!

# KATEGORİ 4 DEVAM: AKADEMİK DANIŞMA (Soru 41-50)

## SORU 41: Tez Savunma Hazırlığı
**Başlık:** Tez savunmasında neler sorarlar?
**Kullanıcı:** SavunmaTelasi | **Tarih:** 19 Aralık 2025 | **Görüntülenme:** 523
**Etiketler:** #TezSavunma #Jüri #Sunum

İlk tez savunmam, çok gerginim. Nelere hazırlanmalıyım?

**✅ EN FAYDA YANIT** (Prof_Deneyimli - 38 beğeni):
**Jüri'nin Tipik Soruları:**
1. "Araştırmanızın özgün katkısı nedir?"
2. "Bu örneklem neden seçildi? Genellenebilir mi?"
3. "Bu test yerine X testini neden kullanmadınız?"
4. "Sınırlılıklar neler?"
5. "Gelecek araştırma önerileri?"

**Hazırlık:**
- **Sunum:** 15-20 dakika, 12-15 slayt
- **Tezini 5 dakikada anlatabilmeli**
- **Metodoloji tartışması:** Neden bu yöntem?
- **Mock defense:** Arkadaşlarla prova yap
- **Rahat kıyafet:** Resmi ama rahat
- **Erken git:** 30 dk önce orada ol

**Jüri Tipleri:**
😊 Destekleyici: Küçük düzeltmeler önerir
😐 Tarafsız: Metodoloji odaklı sorular
😠 Eleştirel: Her şeyi sorguluyor (kişisel alma!)

**SONUÇ:** %95 kabul edilir, sadece küçük revizyonlar istenir.

---

## SORU 42: Akademik Yazım Hataları
**Başlık:** En sık yapılan tez yazım hataları
**Kullanıcı:** YazimDuzeltici | **Tarih:** 18 Aralık 2025 | **Görüntülenme:** 412
**Etiketler:** #AkademikYazım #TezDüzeltme #YazımHataları

Danışmanım sürekli düzeltme istiyor. Nelere dikkat etmeliyim?

**✅ EN FAYDA YANIT** (EditorProf - 30 beğeni):
**Top 10 Yazım Hatası:**

1. **Ben/Biz kullanma** ❌
   - Yanlış: "Biz bu çalışmada..."
   - Doğru: "Bu çalışmada..."

2. **Edilgen çatı fazla** ❌
   - Yanlış: "Veri analiz edilmiştir"
   - Doğru: "Veri analiz edildi" (geçmiş zaman yeterli)

3. **Tutarsız zaman** ❌
   - Literatür tarama: Geniş zaman (vardır, göstermektedir)
   - Yöntem: Geçmiş zaman (toplandı, yapıldı)

4. **Kaynak göstermeme**
   - Her iddia mutlaka kaynaklı olmalı

5. **Gereksiz kelime**
   - "Söz konusu", "bahsetmek gerekirse"

6. **Uzun paragraflar**
   - Max 7-8 satır

7. **Tablo/Şekil metin tekrarı**
   - Tablo zaten gösteriyor, aynen yazma

8. **Yabancı kelime fazla**
   - "feedback" → geri bildirim

9. **Noktalama**
   - Virgül, noktalı virgül uygun kullan

10. **Kısaltma açıklaması yok**
    - İlk kullanımda aç: Dünya Sağlık Örgütü (DSÖ)

---

## SORU 43: Yayın Yapma Süreci
**Başlık:** Uluslararası dergide makale yayınlama
**Kullanıcı:** MakaleGonderici | **Tarih:** 17 Aralık 2025 | **Görüntülenme:** 367
**Etiketler:** #MakaleYayın #PeerReview #Dergi

Tezimden makale çıkarmak istiyorum. Nasıl başlamalıyım?

**✅ EN FAYDA YANIT** (AkademisyenYazar - 28 beğeni):
**Yayın Süreci:**

**1. Hedef Dergi Seç:**
- **Impact Factor (IF)** kontrol et (JCR)
- **Q1-Q2** dergiler tercih et
- **Açık erişim mi? Ücretli mi?** (APC)
- **Scope** uygun mu?

**2. Makaleyi Hazırla:**
- Tez ≠ Makale (daha kısa, öz)
- Dergi formatına uygun (Author Guidelines)
- Abstract: 150-250 kelime
- Anahtar kelime: 4-6
- Referans sayısı: 30-50

**3. Gönder:**
- Online submission sistemi
- Cover letter yaz
- Suggested reviewers öner

**4. Peer Review:**
- Editor'den ret/kabul (2-4 hafta)
- Reviewer'lar inceler (4-12 hafta)
- **Karar:** Kabul / Minor Revision / Major Revision / Ret

**5. Revizyon:**
- Reviewer yorumlarını cevapla (point-by-point)
- Değişiklikleri işaretle
- Tekrar gönder

**6. Yayın:**
- Kabul → Online first (2-4 hafta)
- Basılı sayı (3-6 ay)

**SCI/SSCI dergilerde ortalama süre: 6-12 ay**

**Tavsiye:** Danışmanınla birlikte yazın (co-author).

---

## SORU 44: Anket Uygulaması İpuçları
**Başlık:** Online anket yanıt oranını artırma
**Kullanıcı:** AnketToplamada | **Tarih:** 16 Aralık 2025 | **Görüntülenme:** 298
**Etiketler:** #AnketUygulama #VeriToplama #YanıtOranı

Google Forms ile 500 kişiye gönderdim ama sadece 50 yanıt geldi. Ne yapmalıyım?

**✅ EN FAYDA YANIT** (AnketStratejisti - 26 beğeni):
**Yanıt Oranını Artırma Taktikleri:**

**1. Kısa Tutun:**
- Max 10 dakika (40-50 soru)
- İlerleme çubuğu ekle

**2. Teşvik:**
- Çekiliş yap (5× 100 TL hediye kartı)
- Sonuçları paylaşma vaadi

**3. Kişiselleştir:**
- "Merhaba [Ad]" ile başla
- "Görüşünüz çok önemli" mesajı

**4. Hatırlatma:**
- 3-4 gün sonra gentle reminder
- "Son 24 saat!" aciliyeti

**5. Erişim Kolaylığı:**
- Mobil uyumlu
- QR kod kullan
- Kısa link (bit.ly)

**6. Güven:**
- Üniversite logosu
- Gizlilik bildirimi
- Sonuçların nasıl kullanılacağını açıkla

**7. Doğru Kanal:**
- LinkedIn (profesyoneller için)
- Instagram (gençler için)
- WhatsApp grupları
- Email (kurumsal)

**Beklenti:** %15-20 yanıt oranı normal kabul edilir.

---

## SORU 45: Nitel Araştırma Yöntemleri
**Başlık:** MAXQDA ile nitel veri analizi
**Kullanıcı:** NitelArastirmaci | **Tarih:** 15 Aralık 2025 | **Görüntülenme:** 289
**Etiketler:** #NitelAraştırma #MAXQDA #İçerikAnalizi

Görüşme verilerimi nasıl analiz ederim? Kodlama nedir?

**✅ EN FAYDA YANIT** (NitelUzman - 24 beğeni):
**Nitel Veri Analizi Adımları:**

**1. Veri Hazırlığı:**
- Ses kayıtlarını transkript et (yazıya dök)
- Word/TXT formatında kaydet
- MAXQDA/NVivo'ya yükle

**2. İlk Okuma:**
- Tüm metni oku
- Genel izlenim not et

**3. Kodlama (Coding):**
- **Açık kodlama:** Satır satır oku, önemli kısımları işaretle
- **Kod oluştur:** "Motivasyon eksikliği", "İş tatmini" gibi
- **Axial kodlama:** Kodları kategorilere grupla

**4. Tema Oluşturma:**
- Kategorileri temalar altında topla
- Örnek: "İş Stresi" teması → Alt kodlar: Zaman baskısı, İş yükü, Çatışma

**5. Geçerlilik:**
- **Üçgenleme:** Farklı veri kaynaklarıyla doğrula
- **Katılımcı teyidi:** Sonuçları katılımcıya göster
- **Uzman değerlendirmesi:** Kodlamaları başkasına kontrol ettir

**6. Raporlama:**
- Her tema için **doğrudan alıntılar** ekle:
  > "İş yükü çok fazla, eve götürüyorum..." (K3, Erkek, 35 yaş)

**MAXQDA'da:** Document System'de metinleri seç, Code System'de kodla.

---

## SORU 46: Kariyer Yol Haritası
**Başlık:** Akademik kariyer vs sektör tercihi
**Kullanıcı:** KariyerKararsizi | **Tarih:** 14 Aralık 2025 | **Görüntülenme:** 445
**Etiketler:** #Kariyer #Akademi #Sektör #Doktora

Y. lisans bitiriyorum. Akademide mi kalmalı, sektöre mi geçmeli?

**✅ EN FAYDA YANIT** (KariyerDanismani_PhD - 33 beğeni):
**Akademik Kariyer:**
**Artıları:**
✅ Entelektüel özgürlük
✅ Araştırma yapma fırsatı
✅ Esneklik (kısmen)
✅ Prestij
✅ Yaz tatilleri

**Eksileri:**
❌ Düşük maaş (özellikle başlangıç)
❌ Uzun yol (Doktora 4-6 yıl + Doçentlik)
❌ İş güvencesi zor (kadrolu olmak)
❌ Yayın baskısı
❌ Coğrafi hareketlilik (atama)

---

**Sektör Kariyer:**
**Artıları:**
✅ Yüksek maaş
✅ Hızlı kariyer
✅ Pratik beceriler
✅ Çeşitlilik (farklı projeler)

**Eksileri:**
❌ Monotonluk (rutin)
❌ Az özerklik
❌ Stres (hedefler, satış)
❌ İş güvencesi belirsiz

---

**Kararı Nasıl Ver?**
1. **Doktora yap, sonra karar ver** (akademi kapıları açık kalır)
2. **Hibrit model:** Sektörde çalış + part-time öğretim üyeliği
3. **Kendi kendine sor:** 
   - "10 yıl sonra ne yapıyor olmak isterim?"
   - "Maaş mı, içerik mi öncelikli?"
   - "Ailemi nerede görmek isterim?"

**Not:** Sektörden akademiye geçiş zor. Akademiden sektöre geçiş kolay.

---

## SORU 47: Kongre/Konferans Katılımı
**Başlık:** İlk kez bildiri sunacağım, ne yapmalıyım?
**Kullanıcı:** KongreyeGiden | **Tarih:** 13 Aralık 2025 | **Görüntülenme:** 312
**Etiketler:** #Kongre #Bildiri #Sunum #Networking

Ulusal kongrede bildiri kabul edildi. Sunumu nasıl hazırlamalıyım?

**✅ EN FAYDA YANIT** (KongreGazisi - 27 beğeni):
**Bildiri Sunumu Hazırlık:**

**Sözlü Sunum (10-15 dakika):**
```
Slayt 1: Başlık + İsimler
Slayt 2: Araştırma Problemi
Slayt 3: Literatür (çok kısa!)
Slayt 4: Yöntem (örneklem, veri)
Slayt 5-6: Bulgular (tablo/grafik)
Slayt 7: Sonuç ve Öneriler
Slayt 8: Teşekkür + İletişim
```

**Poster Sunum:**
- A0 boyut (84×119 cm)
- Uzaktan okunabilir (font ≥24)
- Az metin, çok görsel
- QR kod (makalenin linki)

**İpuçları:**
✅ **Prova yap:** Ayna karşısında / arkadaşa
✅ **Zaman tut:** 10 dk'yı geçme
✅ **Sorulara hazırlık:** "Sınırlılıklar?", "Gelecek araştırma?"
✅ **Kartvizit:** İletişim için
✅ **Networking:** Diğer sunumları izle, tanış

**Giyim:** 
- Erkek: Gömlek-pantolon / Takım (kravat şart değil)
- Kadın: Blazer-pantolon / Elbise (rahat ayakkabı)

**Sonrası:**
- LinkedIn'den ekleme yapabilirsin
- Tam metin makale yayınla (proceedings)

---

## SORU 48: Burs ve Fon Kaynakları
**Başlık:** Doktora için burs imkanları neler?
**Kullanıcı:** BursArayan | **Tarih:** 12 Aralık 2025 | **Görüntülenme:** 478
**Etiketler:** #Burs #Doktora #TÜBİTAK #YurtDışı

Doktora yapmak istiyorum ama maddi imkanım yok. Nereden destek alabilirim?

**✅ EN FAYDA YANIT** (BursUzmani - 34 beğeni):
**Türkiye'de Burs Olanakları:**

**1. TÜBİTAK 2211-A (Yurt İçi Doktora):**
- Aylık: ~25,000 TL (2026)
- Süre: 48 ay
- Şartlar: Doktora öğrencisi olma, YÖKSİS girişi
- Başvuru: Yılda 2 kez (Mart-Eylül)
- **Not değer:** 85+

**2. Üniversite Bursu:**
- Aylık: 12,000-20,000 TL
- Her üniversite farklı
- Araştırma görevlisi kadrosuna başvur

**3. YÖK 100/2000 Doktora:**
- Maaş + sosyal haklar
- Özel seçim sınavı
- Çok rekabetçi

**4. Özel Sektör (Google, Microsoft, vb.):**
- Fellowship programları
- Staj + burs

---

**Yurt Dışı Doktora:**

**1. Fulbright (ABD):**
- Tam burs + yaşam gideri
- TOEFL/GRE şart

**2. DAAD (Almanya):**
- Aylık €1,200
- Almanca/İngilizce

**3. Erasmus+ (Avrupa):**
- 3-12 ay değişim
- Aylık €1,000-1,500

**4. Chevening (İngiltere):**
- Master için (Doktora değil)

**Başvuru İpuçları:**
- **Erken başla:** 6-12 ay önceden
- **Statement of Purpose:** İyi yaz
- **Referans mektupları:** Güçlü olsun
- **CV:** Yayın, proje, staj ekle

---

## SORU 49: Araştırma Etiği İhlalleri
**Başlık:** İntihal nedir ve nasıl önlenir?
**Kullanıcı:** EtikMerakli | **Tarih:** 11 Aralık 2025 | **Görüntülenme:** 389
**Etiketler:** #İntihal #AraştırmaEtiği #Turnitin

Tezimde intihal oranı %18 çıktı. Bu kabul edilir mi?

**✅ EN FAYDA YANIT** (EtikKuruluUyesi_Prof - 29 beğeni):
**İntihal Türleri:**

1. **Doğrudan intihal:**
   - Başkasının yazısını aynen kopyala-yapıştır
   - **Çok ciddi ihlal!**

2. **Mozaik intihal:**
   - Cümleleri değiştir ama kaynak gösterme
   - Yine ihlal!

3. **Self-plagiarism:**
   - Kendi eski yazından alıntı (kaynak göstermeden)
   - Bu da yasak!

4. **Yanlış atıf:**
   - Kaynağı okumadan referans göster
   - Etik ihlal

---

**Turnitin/iThenticate Oranları:**
- **0-10%:** Mükemmel ✅
- **10-15%:** Kabul edilebilir (kaynakça, alıntılar)
- **15-25%:** Şüpheli (kontrol gerek)
- **25%+:** Ciddi sorun ❌

**Senin durumun (%18):**
- Kaynakça uzunsa normal olabilir
- Doğrudan alıntılar fazla mı?
- Teorik çerçeve standart ifadeler mi?

---

**Nasıl Önlenir?**
✅ **Paraphrase et:** Cümleyi kendi kelimerinle yaz
✅ **Kaynak göster:** Her fikir için
✅ **Quotation marks:** Doğrudan alıntıda tırnak
✅ **Referans yöneticisi kullan:** Mendeley, Zotero

**Yanlış:**
> "İnsan kaynakları yönetimi, organizasyonların başarısında kritik rol oynar."

**Doğru:**
> İnsan kaynakları yönetimi, örgütsel başarıda önemli bir faktördür (Smith, 2020).

---

## SORU 50: Stres Yönetimi (Tez Sürecinde)
**Başlık:** Tez yazarken tükenmişlik yaşıyorum
**Kullanıcı:** StresliYazar | **Tarih:** 10 Aralık 2025 | **Görüntülenme:** 512
**Etiketler:** #Stres #Tükenmişlik #MentalSağlık #TezSüreci

Tez yazarken her şey çok yoğun. Nasıl başa çıkmalıyım?

**✅ EN FAYDA YANIT** (PsikolojikDanışman_PhD - 36 beğeni):
**Akademik Tükenmişlik Sinyalleri:**
❌ Sürekli yorgunluk
❌ Motivasyon kaybı
❌ Uyku bozukluğu
❌ "Hiç bitmeyecek" hissi
❌ Sosyal izolasyon

**Başa Çıkma Stratejileri:**

**1. Küçük Hedefler:**
- "Tezi bitir" değil → "Bugün 2 sayfa yaz"
- **Pomodoro:** 25 dk çalış, 5 dk mola

**2. Rutine Geç:**
- Her gün aynı saatte çalış
- Hafta sonu tamamen ara ver

**3. Sosyal Destek:**
- Tez arkadaşları edin
- "Writing group" oluştur
- Danışmanla düzenli görüş

**4. Fiziksel Aktivite:**
- Günde 30 dk yürüyüş
- Spor = stres atma

**5. Gerçekçi Beklenti:**
- Mükemmel tez yok
- "Good enough" yeterli
- Danışman memnunsa yeterli

**6. Profesyonel Yardım:**
- Üniversite psikolojik danışmanlık merkezi (ÜCRETSİZ)
- "Terapiye gitmek zaaf değil!"

**7. Self-Care:**
- Düzenli uyku (7-8 saat)
- Sağlıklı beslen
- Hobi yap (tezden bağımsız)

**Hatırla:** Tez bir maraton, sprint değil. Kendi hızında ilerle!

**ACİL DURUM:** İntihar düşüncesi → Hemen yardım: 182 (Psikolojik Destek)

---

# BONUS: KULLANICI PROFİLLERİ

**Dr_Mehmet_Stats**
- Biyoistatistik Doçenti
- 500+ yanıt, 2500+ beğeni
- Uzmanlık: SPSS, İstatistik teorisi, Tez danışmanlığı
- Rozetler: 🏆 Topluluk Lideri, 📊 İstatistik Gurusu

**PythonGurusu**
- Veri Bilimci (sektör)
- 300+ yanıt, 1800+ beğeni
- Uzmanlık: Python, Pandas, Machine Learning
- Rozetler: 🐍 Python Ninja, 💻 Kod Ustası

**R_Uzmani**
- Ekonometri Araştırmacısı
- 200+ yanıt, 1200+ beğeni
- Uzmanlık: R Studio, Zaman serisi, Regresyon
- Rozetler: 📈 R Uzmanı, 🔬 Araştırma Yıldızı

**AnalizMeraklisi**
- Y. Lisans Öğrencisi (Eğitim Bilimleri)
- 80+ yanıt, 450+ beğeni
- Uzmanlık: SPSS temel, Anket tasarımı
- Rozetler: 🎓 Yardımsever, ⭐ Yükselen Yetenek

**TezDanismani_Prof**
- Üniversite Profesörü (Psikoloji)
- 150+ yanıt, 1100+ beğeni
- Uzmanlık: Metodoloji, Nitel araştırma, Tez yazımı
- Rozetler: 👨‍🏫 Mentor, 📚 Bilge

**MetodologiUzmani**
- Araştırma Görevlisi (Sosyoloji)
- 120+ yanıt, 700+ beğeni
- Uzmanlık: Karma yöntem, SEM, Meta-analiz
- Rozetler: 🔍 Metodoloji Şampiyonu

---

# ETİKET SİSTEMİ

**Yazılım Etiketleri:**
#SPSS #Python #R #AMOS #MAXQDA #NVivo #Jamovi #JASP #Excel #Stata

**Analiz Etiketleri:**
#T-Test #ANOVA #Regresyon #Korelasyon #ChiSquare #FaktorAnalizi #SEM #Mediation #Moderation

**Metodoloji Etiketleri:**
#NormallikTesti #Güvenilirlik #Geçerlilik #Örneklem #Varsayımlar #ExpertPanel

**Akademik Etiketleri:**
#TezYazımı #LiteratürTaraması #MakaleYayın #EtikKurul #Kongre #Burs #APA7

**Seviye Etiketleri:**
#YeniBaslayan #Orta #İleri #Uzman

---

# ÖZET İSTATİSTİKLER

**Toplam İçerik:** 50 Soru-Yanıt Seti
- SPSS: 15 soru
- Python/R: 10 soru
- Analiz Yöntemleri: 10 soru
- Akademik Danışma: 15 soru

**Toplam Kelime:** ~18,000
**Ortalama Görüntülenme:** 300+
**Çözülmüş Sorular:** 20 adet (✅ işaretli)
**En Popüler:** Örneklem büyüklüğü (567 görüntülenme)

**Kullanıcı Tipleri:**
- Yeni başlayan öğrenciler: 40%
- Y. Lisans öğrencileri: 30%
- Araştırma görevlileri: 20%
- Profesyoneller: 10%

