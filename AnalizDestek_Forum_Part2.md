```markdown
# 📊 ANALİZ DESTEK FORUM İÇERİK PAKETİ - BÖLÜM 2
> **Kapsam:** Python, R, Excel, Yapay Zeka, Akademik Yazım
> **Durum:** Hazır ve Onaylı

---

# 🐍 KATEGORİ: PYTHON & VERİ BİLİMİ

## SORU 1: Pandas GroupBy Kullanımı ✅ ÇÖZÜLDÜ
**Başlık:** Pandas ile gruplayarak ortalama alma (GroupBy)
**Kullanıcı:** PyDataAnalist | **Tarih:** 15 Ocak 2026 | **Görüntülenme:** 142
**Etiketler:** #Python #Pandas #DataAnalysis

Elimde bir satış verisi var. "Şehir" bazında toplam satışları nasıl hesaplarım? Kodlarımı aşağıya bırakıyorum ama hata alıyorum.

**✅ EN FAYDALI YANIT** (PythonGurusu - 18 beğeni):
Çok basit! `groupby` fonksiyonu bu işin temelidir:
```python
df.groupby('Sehir')['SatisTutari'].sum()

```

Eğer hem ortalama hem toplam istersen `.agg(['mean', 'sum'])` kullanabilirsin.

---

## SORU 2: Matplotlib Türkçe Karakter

**Başlık:** Grafiklerimde Türkçe karakterler kare (□) çıkıyor!
**Kullanıcı:** GorselHata | **Tarih:** 14 Ocak 2026 | **Görüntülenme:** 98
**Etiketler:** #Matplotlib #Visualization #HataÇözümü

Python'da çizdirdiğim grafiklerde "ş, ı, ğ" harfleri bozuk görünüyor. Font ayarı mı yapmam lazım?

**✅ EN FAYDALI YANIT** (KodMimari - 15 beğeni):
Matplotlib varsayılan fontu Türkçe desteklemiyor olabilir. Şunu kodun başına ekle:

```python
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'DejaVu Sans'
# Veya Windows kullanıyorsan 'Arial' dene

```

---

## SORU 3: Scikit-Learn Train/Test

**Başlık:** Veriyi eğitim ve test olarak nasıl bölerim?
**Kullanıcı:** ML_Ogrenci | **Tarih:** 13 Ocak 2026 | **Görüntülenme:** 210
**Etiketler:** #MachineLearning #Sklearn #VeriBilimi

Model eğitmeden önce veriyi %80-%20 ayırmak istiyorum. Manuel mi yapmalıyım?

**✅ EN FAYDALI YANIT** (AI_Uzmani - 22 beğeni):
Manuel yapma, veri dağılımını bozabilirsin. Standart yöntem `train_test_split` kullanmaktır:

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

```

`random_state=42` yazmayı unutma, sonuçların tekrarlanabilir olsun!

---

## SORU 4: Jupyter Notebook Kernel Died

**Başlık:** Sürekli "Kernel Restarting" hatası alıyorum
**Kullanıcı:** RamSorunu | **Tarih:** 12 Ocak 2026 | **Görüntülenme:** 305
**Etiketler:** #Jupyter #Hata #Bellek

Büyük bir veri seti (2GB) okurken notebook çöküyor ve bağlantı kopuyor.

**✅ EN FAYDALI YANIT** (SysAdmin_Tr - 19 beğeni):
Muhtemelen RAM yetmiyor. Pandas ile okurken `chunksize` parametresini kullanmayı dene veya veri tiplerini optimize et (örn: `float64` yerine `float32`). Alternatif olarak Google Colab kullanabilirsin.

---

## SORU 5: Web Scraping İzni

**Başlık:** Tez için web sitesinden veri çekmek yasal mı?
**Kullanıcı:** VeriMadencisi | **Tarih:** 11 Ocak 2026 | **Görüntülenme:** 450
**Etiketler:** #WebScraping #Etik #BeautifulSoup

Bir e-ticaret sitesinden fiyatları çekip analiz etmek istiyorum. Etik kurul onayı gerekir mi?

**✅ EN FAYDALI YANIT** (HukukVeBilisim - 35 beğeni):
Akademik amaçlı ve "sunucuyu yormadan" (time.sleep koyarak) çekersen genelde sorun olmaz. Ancak veriyi **ticari amaçla kullanamazsın** ve yayınlarken anonimleştirmen gerekir. Sitenin `robots.txt` dosyasını mutlaka kontrol et!

---

# 📈 KATEGORİ: R DİLİ & R STUDIO

## SORU 1: ggplot2 Renk Değiştirme ✅ ÇÖZÜLDÜ

**Başlık:** ggplot2 grafiklerinde renkleri manuel ayarlama
**Kullanıcı:** R_Artist | **Tarih:** 15 Ocak 2026 | **Görüntülenme:** 120
**Etiketler:** #RStudio #ggplot2 #Görselleştirme

Otomatik renkleri sevmedim. Kendi istediğim renkleri (kurumsal renklerimizi) nasıl veririm?

**✅ EN FAYDALI YANIT** (R_Uzmani - 14 beğeni):
`scale_fill_manual()` fonksiyonunu kullanmalısın:

```r
ggplot(df, aes(x=Grup, y=Deger, fill=Grup)) +
  geom_bar(stat="identity") +
  scale_fill_manual(values=c("red", "blue", "#00d2ff"))

```

---

## SORU 2: Dplyr Filter

**Başlık:** Birden fazla koşula göre filtreleme (dplyr)
**Kullanıcı:** VeriAyiklayici | **Tarih:** 14 Ocak 2026 | **Görüntülenme:** 156
**Etiketler:** #R #Dplyr #DataManipulation

Hem "Erkek" olanları hem de "Yaşı 25'ten büyük" olanları nasıl seçerim?

**✅ EN FAYDALI YANIT** (TidyverseFan - 20 beğeni):
Dplyr kütüphanesi ile pipe operatörünü kullanarak çok kolay yapabilirsin:

```r
library(dplyr)
yeni_veri <- veri %>% 
  filter(Cinsiyet == "Erkek" & Yas > 25)

```

---

## SORU 3: R Paket Yükleme Hatası

**Başlık:** "There is no package called..." hatası alıyorum
**Kullanıcı:** YeniRci | **Tarih:** 13 Ocak 2026 | **Görüntülenme:** 189
**Etiketler:** #RStudio #Hata #Library

Kodu çalıştırıyorum ama kütüphane bulunamadı diyor.

**✅ EN FAYDALI YANIT** (R_Uzmani - 12 beğeni):
Kütüphaneyi çağırmadan önce bilgisayarına indirmen lazım. Şu kodu bir kere çalıştır:
`install.packages("paket_adi")`
Sonra `library(paket_adi)` diyerek kullanabilirsin.

---

## SORU 4: R Markdown Rapor

**Başlık:** Analizleri Word çıktısı olarak almak
**Kullanıcı:** TezYazimiR | **Tarih:** 12 Ocak 2026 | **Görüntülenme:** 245
**Etiketler:** #RMarkdown #Raporlama #Knit

Kodları ve grafikleri kopyala yapıştır yapmadan direkt Word'e aktarabilir miyim?

**✅ EN FAYDALI YANIT** (AkademikR - 28 beğeni):
Kesinlikle! R Markdown (.Rmd) dosyası oluştur. Başlık kısmına (YAML) şunu yaz:

```yaml
output: word_document

```

Sonra "Knit" butonuna basınca tertemiz bir Word raporu alırsın.

---

## SORU 5: Korelasyon Matrisi

**Başlık:** R'da tüm değişkenlerin korelasyonuna bakmak
**Kullanıcı:** Istatistikci | **Tarih:** 11 Ocak 2026 | **Görüntülenme:** 167
**Etiketler:** #Korelasyon #R #Cor

Elimde 10 değişken var, hepsinin birbirine korelasyonunu tek tabloda görmek istiyorum.

**✅ EN FAYDALI YANIT** (R_Uzmani - 15 beğeni):
Sadece sayısal sütunları seçip `cor()` fonksiyonuna ver:

```r
sayisal_veri <- veri[sapply(veri, is.numeric)]
cor(sayisal_veri, use="complete.obs")

```

Görselleştirmek için `corrplot` kütüphanesini öneririm.

---

# 📊 KATEGORİ: EXCEL & İŞ ZEKASI

## SORU 1: VLOOKUP vs XLOOKUP ✅ ÇÖZÜLDÜ

**Başlık:** Düşeyara (VLOOKUP) yerine ne kullanmalıyım?
**Kullanıcı:** ExcelSeven | **Tarih:** 15 Ocak 2026 | **Görüntülenme:** 320
**Etiketler:** #Excel #Formül #XLOOKUP

Düşeyara soldaki sütunu getiremiyor, sütun ekleyince formül bozuluyor. Çok sinir bozucu!

**✅ EN FAYDALI YANIT** (OfisGurusu - 45 beğeni):
Hocam devir değişti, artık **ÇAPRAZARA (XLOOKUP)** var! Hem sağa hem sola bakabilir, hata yönetimi (bulunamazsa) içindedir ve sütun eklense de bozulmaz.
`=ÇAPRAZARA(Aranan; Aranan_Dizi; Döndürülen_Dizi)`

---

## SORU 2: Pivot Tablo Yüzde

**Başlık:** Pivot Tabloda satır toplamı yüzdesi gösterme
**Kullanıcı:** Raporcu | **Tarih:** 14 Ocak 2026 | **Görüntülenme:** 210
**Etiketler:** #PivotTable #Excel #Raporlama

Sayıları değil de oranları (%) göstermek istiyorum.

**✅ EN FAYDALI YANIT** (ExcelMaster - 22 beğeni):
Değer alanındaki sayıya sağ tıkla > **Değer Gösterimi (Show Values As)** > **Satır Toplamı Yüzdesi (% of Row Total)** seçeneğini seç.

---

## SORU 3: Power BI Veri Yenileme

**Başlık:** Excel'i güncelleyince Power BI otomatik güncellenir mi?
**Kullanıcı:** BIDeveloper | **Tarih:** 13 Ocak 2026 | **Görüntülenme:** 180
**Etiketler:** #PowerBI #VeriYenileme #Dashboard

Raporu yayınladım, kaynak excel değişince rapordaki grafikler değişmiyor.

**✅ EN FAYDALI YANIT** (DashboardUzmani - 25 beğeni):
Masaüstü sürümünde "Yenile" (Refresh) butonuna basman lazım. Bulutta (Power BI Service) ise bilgisayarına "Gateway" kurarak otomatik yenileme zamanlaması (Scheduled Refresh) ayarlayabilirsin.

---

## SORU 4: Koşullu Biçimlendirme

**Başlık:** Belli bir değerden büyükleri kırmızı yapmak
**Kullanıcı:** GorselExcel | **Tarih:** 12 Ocak 2026 | **Görüntülenme:** 145
**Etiketler:** #Excel #Format #Görselleştirme

50'den düşük not alan öğrencilerin hücresi otomatik kırmızı olsun istiyorum.

**✅ EN FAYDALI YANIT** (OfisGurusu - 18 beğeni):
Hücreleri seç > Giriş > **Koşullu Biçimlendirme** > Hücre Kurallarını Vurgula > **Küçüktür...** > 50 yaz ve Kırmızı Dolgu seç.

---

## SORU 5: Excel Makro Güvenliği

**Başlık:** Makrolar çalışmıyor, "Güvenlik Riski" diyor
**Kullanıcı:** Otomasyoncu | **Tarih:** 11 Ocak 2026 | **Görüntülenme:** 290
**Etiketler:** #VBA #Makro #Güvenlik

İnternetten indirdiğim makrolu dosyayı açamıyorum, kırmızı bir şerit çıkıyor.

**✅ EN FAYDALI YANIT** (VBACoder - 30 beğeni):
Dosyaya sağ tıkla > **Özellikler** > En altta "Engellemeyi Kaldır" (Unblock) kutucuğunu işaretle. Microsoft güvenlik nedeniyle internetten gelen makroları artık varsayılan olarak engelliyor.

---

# 🤖 KATEGORİ: YAPAY ZEKA & DL

## SORU 1: ChatGPT Literatür Taraması ✅ ÇÖZÜLDÜ

**Başlık:** Tez yazarken ChatGPT kullanmak intihal mi?
**Kullanıcı:** EtikAI | **Tarih:** 15 Ocak 2026 | **Görüntülenme:** 850
**Etiketler:** #YapayZeka #TezYazımı #Etik

ChatGPT'ye literatür özeti yazdırsam sorun olur mu? Turnitin yakalar mı?

**✅ EN FAYDALI YANIT** (AkademikEtik - 60 beğeni):
ChatGPT bir araçtır, yazar değildir. Fikir almak, dil düzeltmek için kullanabilirsin ama **çıktıyı kopyala-yapıştır yaparsan intihaldir (AI-generated content).** Ayrıca kaynakları uydurabilir (halüsinasyon), mutlaka orijinal makaleyi bulup oku!

---

## SORU 2: CNN Nedir?

**Başlık:** Görüntü işleme için neden CNN kullanıyoruz?
**Kullanıcı:** DeepLearner | **Tarih:** 14 Ocak 2026 | **Görüntülenme:** 310
**Etiketler:** #DeepLearning #CNN #ComputerVision

Normal sinir ağları (ANN) resimlerde işe yaramaz mı?

**✅ EN FAYDALI YANIT** (AI_Researcher - 42 beğeni):
CNN (Evrişimli Sinir Ağları), resimdeki kenar, köşe, doku gibi özellikleri (spatial features) koruyarak öğrenir. Normal ANN'de resmi düzleştirince (flatten) bu uzaysal ilişkiler kaybolur ve işlem yükü aşırı artar.

---

## SORU 3: Overfitting (Aşırı Öğrenme)

**Başlık:** Modelim eğitimde %99, testte %60 başarı veriyor
**Kullanıcı:** ModelEgitmeni | **Tarih:** 13 Ocak 2026 | **Görüntülenme:** 275
**Etiketler:** #MachineLearning #Overfitting #Hata

Bu farkın sebebi nedir? Modelim ezberliyor mu?

**✅ EN FAYDALI YANIT** (VeriBilimci - 35 beğeni):
Evet, buna **Overfitting (Ezberleme)** denir. Modelin veriyi öğrenmek yerine ezberlemiş.
Çözümler:

1. Daha fazla veri topla.
2. Modeli basitleştir (katman azalt).
3. **Dropout** veya **Regularization (L1/L2)** ekle.

---

## SORU 4: Python Keras vs PyTorch

**Başlık:** Yeni başlayan biri hangisini seçmeli?
**Kullanıcı:** FrameworkSecimi | **Tarih:** 12 Ocak 2026 | **Görüntülenme:** 400
**Etiketler:** #DeepLearning #Keras #PyTorch

Hızlıca proje geliştirmek istiyorum. Hangisi daha kolay?

**✅ EN FAYDALI YANIT** (KodMimari - 28 beğeni):
Hızlı prototip ve kolaylık için **Keras (TensorFlow)**. Araştırma yapacaksan, modelin içini mıncıklamak ve esneklik lazımsa **PyTorch**. Sektörde ikisi de popüler ama akademi PyTorch'a kayıyor.

---

## SORU 5: NLP Duygu Analizi

**Başlık:** Türkçe metinlerde duygu analizi yapmak
**Kullanıcı:** MetinMadencisi | **Tarih:** 11 Ocak 2026 | **Görüntülenme:** 230
**Etiketler:** #NLP #SentimentAnalysis #Bert

Türkçe tweetleri olumlu/olumsuz diye ayırmak istiyorum.

**✅ EN FAYDALI YANIT** (NLPEngineer - 33 beğeni):
Klasik yöntemler yerine **BERTurk** modelini kullanmanı öneririm. Hugging Face kütüphanesinde hazır eğitilmiş Türkçe modeller var, başarı oranı çok daha yüksek.

---

# 📝 KATEGORİ: RAPORLAMA & YAZIM

## SORU 1: Zotero vs Mendeley ✅ ÇÖZÜLDÜ

**Başlık:** Kaynakça yönetimi için hangisi daha iyi?
**Kullanıcı:** KaynakcaMagduru | **Tarih:** 15 Ocak 2026 | **Görüntülenme:** 340
**Etiketler:** #Referans #Zotero #Mendeley #TezYazımı

Word eklentisi en sorunsuz çalışan hangisi? Mendeley sürekli çöküyor.

**✅ EN FAYDALI YANIT** (AkademikAsistan - 40 beğeni):
**Zotero** açık kaynaklıdır ve tamamen ücretsizdir, tarayıcı eklentisi mükemmel çalışır. Mendeley son güncellemelerle biraz hantallaştı. Zotero + Word eklentisi şu an en sağlam kombinasyon.

---

## SORU 2: Edilgen Çatı Kullanımı

**Başlık:** Tezde "Ben yaptım" mı "Yapıldı" mı denmeli?
**Kullanıcı:** YazimKurallari | **Tarih:** 14 Ocak 2026 | **Görüntülenme:** 290
**Etiketler:** #AkademikDil #Yazım #TÜBİTAK

Danışmanım "Ben" dilini yasakladı, ama İngilizce makalelerde "We" görüyorum.

**✅ EN FAYDALI YANIT** (EditorProf - 55 beğeni):
Türkçe akademik dilde kural **nesnel ve edilgen** olmasıdır.
❌ "Anketi öğrencilere uyguladım."
✅ "Anket öğrencilere uygulanmıştır."
Son yıllarda APA 7, "aktif çatı" kullanımına (bu çalışmada biz...) biraz daha ılımlı bakıyor ama Türkiye'de hala edilgen tercih edilir.

---

## SORU 3: Tablo ve Şekil Atıfı

**Başlık:** Tabloyu metin içinde nasıl anlatmalıyım?
**Kullanıcı:** TabloTasari | **Tarih:** 13 Ocak 2026 | **Görüntülenme:** 180
**Etiketler:** #APA7 #Tablo #Raporlama

Tablodaki her sayıyı metne yazmalı mıyım? Tekrar olmuyor mu?

**✅ EN FAYDALI YANIT** (TezDanismani - 32 beğeni):
Hayır, hepsini yazma! Tablo zaten veriyi gösteriyor. Metinde sadece **önemli bulguları, en yüksek/en düşük değerleri ve anlamlı farkları** vurgula. "Tablo 1'de görüldüğü üzere..." şeklinde atıf yapmayı unutma.

---

## SORU 4: İntihal Oranı Düşürme

**Başlık:** Turnitin oranı %25 çıktı, nasıl düşürürüm?
**Kullanıcı:** PanikAtak | **Tarih:** 12 Ocak 2026 | **Görüntülenme:** 600
**Etiketler:** #İntihal #Turnitin #Paraphrasing

Alıntıları tırnak içine aldım ama yine de yüksek çıkıyor. Ne yapmalıyım?

**✅ EN FAYDALI YANIT** (EtikKurulu - 45 beğeni):
Sadece kelimeleri değiştirmek (eş anlamlı kullanmak) yetmez, **cümle yapısını (sentaks)** değiştirmelisin (Paraphrasing). Ayrıca doğrudan alıntıları azaltıp, okuduğunu kendi yorumunla sentezleyerek yazmalısın.

---

## SORU 5: Özet (Abstract) Yazımı

**Başlık:** İyi bir tez özeti kaç kelime olmalı?
**Kullanıcı:** SonDuzluk | **Tarih:** 11 Ocak 2026 | **Görüntülenme:** 310
**Etiketler:** #Özet #Abstract #Tez

Özette kaynakça verilir mi? Kaç paragraf olmalı?

**✅ EN FAYDALI YANIT** (AkademikYazar - 38 beğeni):
Genelde 150-250 kelime arasıdır ve tek paragraf olması tercih edilir.
Sırasıyla şunları içermeli:

1. Amaç (1 cümle)
2. Yöntem (Evren, örneklem, araçlar)
3. Bulgular (En önemli sonuçlar)
4. Sonuç/Öneri.
❌ Özette asla kaynakça, tablo veya şekil bulunmaz!

```

```