# 📊 ANALİZUS STRATEJİK İÇERİK PAKETİ - BÖLÜM 3
> **Kapsam:** Excel, Nitel Analiz, Diğer Yazılımlar, Regresyon, Yapay Zeka, Bibliyometrik Analiz
> **Hedef:** Forum doluluk oranını %100'e ulaştırmak.

---

# 📑 KATEGORİ: EXCEL & İŞ ZEKASI (5 İÇERİK)

## SORU 1: Dinamik Dashboard Oluşturma ✅ ÇÖZÜLDÜ
**Başlık:** Excel'de otomatik güncellenen Dashboard nasıl yapılır?
**Kullanıcı:** VeriGorselci | **Tarih:** 16 Ocak 2026
Verilerimi her hafta güncelliyorum, grafiklerin manuel kaydırılmadan otomatik büyümesini nasıl sağlarım?
**✅ YANIT:** Verilerini "Tablo" (Ctrl+L) formatına sokmalısın. Grafik veri kaynağı tablo olursa, yeni veri eklediğinde grafik otomatik genişler. Pivot Table kullanıyorsan "Dilimleyici" (Slicer) eklemeyi unutma!

## SORU 2: Power Query ile Veri Birleştirme
**Başlık:** 10 farklı Excel dosyasını tek tabloda toplamak
**Kullanıcı:** MuhasebeUzmani | **Tarih:** 15 Ocak 2026
Farklı şubelerden gelen aylık raporları tek bir ana tabloda nasıl birleştiririm?
**✅ YANIT:** Veri sekmesinden "Verileri Al" > "Dosyadan" > "Klasörden" yolunu izle. Power Query tüm dosyaları sütun başlıklarına göre eşleştirip saniyeler içinde birleştirir.

## SORU 3: Makro Güvenlik Sorunu
**Başlık:** Excel'de "Makrolar devre dışı bırakıldı" hatası
**Kullanıcı:** Otomasyoncu | **Tarih:** 14 Ocak 2026
Yazdığım VBA kodları başka bilgisayarda çalışmıyor, neden?
**✅ YANIT:** Dosya > Seçenekler > Güven Merkezi > Makro Ayarları'ndan "Tüm makroları etkinleştir" seçilmeli. Ayrıca dosyanın `.xlsx` değil, `.xlsm` formatında kaydedildiğinden emin ol.

## SORU 4: Koşullu Biçimlendirme Formülleri
**Başlık:** Hücre değerine göre tüm satırı renklendirme
**Kullanıcı:** Planlama_Y | **Tarih:** 13 Ocak 2026
Sadece tek hücreyi değil, durum "Tamamlandı" ise tüm satırı yeşil yapmak istiyorum.
**✅ YANIT:** Koşullu Biçimlendirme > Yeni Kural > "Biçimlendirilecek hücreleri belirlemek için formül kullan" seç. Formüle `=$C2="Tamamlandı"` yaz (Dolar işareti sadece sütunda kalmalı).

## SORU 5: Excel vs Power BI
**Başlık:** Büyük veri setleri için Excel yeterli mi?
**Kullanıcı:** StratejiAnalisti | **Tarih:** 12 Ocak 2026
1 milyon satırın üzerindeki verilerde Excel çok kasıyor, Power BI'a geçmeli miyim?
**✅ YANIT:** Kesinlikle evet. Excel'in satır limiti 1.048.576'dır. Power BI ise "Veri Modeli" mimarisiyle milyonlarca satırı saniyeler içinde işleyebilir.

---

# 🎙️ KATEGORİ: NİTEL ANALİZ ARAÇLARI (MAXQDA, NVivo) (5 İÇERİK)

## SORU 1: MAXQDA Kodlama Mantığı ✅ ÇÖZÜLDÜ
**Başlık:** Mülakat metinlerini kodlarken nelere dikkat edilmeli?
**Kullanıcı:** Sosyolog_N | **Tarih:** 16 Ocak 2026
MAXQDA'da çok fazla kod oluşturmak analizi zorlaştırır mı?
**✅ YANIT:** Başlangıçta "Açık Kodlama" yaparken cömert olabilirsin ama sonra bu kodları hiyerarşik temalar altında toplamalısın. "Kod Ağacı" çok karmaşıksa analizde kaybolabilirsin.

## SORU 2: NVivo Resim Analizi
**Başlık:** NVivo ile fotoğraf ve video kodlanabilir mi?
**Kullanıcı:** GorselAnaliz | **Tarih:** 15 Ocak 2026
Etnografik çalışmamda fotoğrafları analiz birimi olarak kullanabilir miyim?
**✅ YANIT:** Evet, NVivo'da resim dosyalarını içe aktarıp belirli bölgeleri (region) kare içine alarak kodlayabilirsin. Her bölgeye ayrı notlar eklemek mümkün.

## SORU 3: Transkripsiyon Yazılımları
**Başlık:** Ses kayıtlarını metne dönüştüren en iyi araç hangisi?
**Kullanıcı:** Sahada_Arastirma | **Tarih:** 14 Ocak 2026
Mülakatları tek tek elle yazmak çok vakit alıyor. Yapay zeka çözümü var mı?
**✅ YANIT:** Türkçe için "Otter.ai" zayıf kalsa da, "Whisper AI" veya yerli "Voiser" oldukça başarılı. Metne çevirdikten sonra MAXQDA'ya `.docx` olarak aktarabilirsin.

## SORU 4: Nitel Veride Geçerlilik (Kappa)
**Başlık:** İki farklı kodlayıcı arasındaki uyum (Inter-coder Reliability)
**Kullanıcı:** AkademikEtik | **Tarih:** 13 Ocak 2026
Aynı metni iki kişi kodladık, uyum oranını nasıl raporlamalıyız?
**✅ YANIT:** MAXQDA içinde "Kullanıcılar Arası Uyumu Kontrol Et" aracı vardır. Cohen’s Kappa katsayısının 0.70 üzerinde olması akademik olarak kabul edilebilirdir.

## SORU 5: Kelime Bulutu Oluşturma
**Başlık:** En sık geçen kavramları görselleştirme
**Kullanıcı:** Iletisimci | **Tarih:** 12 Ocak 2026
Odak grup görüşmelerinde en çok kullanılan kelimeleri nasıl raporlarım?
**✅ YANIT:** "Kelime Bulutu" (Word Cloud) aracını kullan. Ancak "ve, ama, gibi" gibi anlam taşımayan kelimeleri "Stop Word List" (Hariç Tutulanlar) listesine eklemeyi unutma.

---

# ⚙️ KATEGORİ: DİĞER ARAÇLAR (STATA, MATLAB) (5 İÇERİK)

## SORU 1: Stata Panel Veri Analizi ✅ ÇÖZÜLDÜ
**Başlık:** Panel veride Fixed Effects vs Random Effects?
**Kullanıcı:** Ekonometrist | **Tarih:** 16 Ocak 2026
Hangisini seçeceğime nasıl karar veririm?
**✅ YANIT:** Stata'da `hausman` testini kullanmalısın. Eğer p < 0.05 ise Fixed Effects (Sabit Etkiler) modelini kullanman gerekir.

## SORU 2: MATLAB'da Grafik Özelleştirme
**Başlık:** MATLAB plot renklerini ve kalınlıklarını ayarlama
**Kullanıcı:** Muhendislik_R | **Tarih:** 15 Ocak 2026
Makale için yüksek çözünürlüklü grafik çıktısı nasıl alınır?
**✅ YANIT:** `plot(x,y,'LineWidth',2,'Color','r')` komutunu kullan. Çıktı alırken `exportgraphics` fonksiyonu ile 300 DPI çözünürlükte `.tiff` veya `.pdf` kaydet.

## SORU 3: Stata Do-File Kullanımı
**Başlık:** Analizlerimi neden Do-File ile kaydetmeliyim?
**Kullanıcı:** VeriBilimci_A | **Tarih:** 14 Ocak 2026
Komut penceresinden yazmak daha hızlı değil mi?
**✅ YANIT:** Hayır, Do-File analizin "kara kutusu"dur. Hata yaptığında veya hakem düzeltme istediğinde tek tıkla her şeyi en baştan hatasız çalıştırabilirsin.

## SORU 4: MATLAB Derin Öğrenme Araç Kutusu
**Başlık:** MATLAB ile hazır yapay zeka modelleri kullanılabilir mi?
**Kullanıcı:** AI_Ogrenci | **Tarih:** 13 Ocak 2026
Resim sınıflandırma için hazır modeller var mı?
**✅ YANIT:** "Deep Learning Toolbox" içinde AlexNet, GoogLeNet gibi önceden eğitilmiş modelleri saniyeler içinde çağırıp kendi verilerinle "Transfer Learning" yapabilirsin.

## SORU 5: Stata'da Veri Temizleme
**Başlık:** Eksik verileri (Missing Values) toplu silme
**Kullanıcı:** SaglikIst | **Tarih:** 12 Ocak 2026
`drop if missing(var)` komutu güvenli mi?
**✅ YANIT:** Güvenlidir ancak veri kaybına yol açar. Önce `mdesc` komutuyla eksiklik oranına bak, eğer oran %5'ten azsa silebilirsin, fazlaysa "Multiple Imputation" yöntemini düşün.

---

# 🔗 KATEGORİ: İLİŞKİ & REGRESYON (5 İÇERİK)

## SORU 1: Lojistik Regresyon Yorumlama ✅ ÇÖZÜLDÜ
**Başlık:** Odds Ratio (Olasılıklar Oranı) nedir?
**Kullanıcı:** Klinik_Aras | **Tarih:** 16 Ocak 2026
Lojistik regresyon sonucunda çıkan Exp(B) değerini nasıl okurum?
**✅ YANIT:** Exp(B) > 1 ise bağımsız değişken bağımlı değişkenin gerçekleşme olasılığını artırıyor demektir. Örneğin 1.50 çıktıysa, o durumun görülme olasılığı %50 artıyor demektir.

## SORU 2: Çoklu Doğrusal Bağlantı (Multicollinearity)
**Başlık:** VIF değerleri kaç olmalı?
**Kullanıcı:** Ekonometri_S | **Tarih:** 15 Ocak 2026
Bağımsız değişkenlerim birbirine çok benziyor, model bozulur mu?
**✅ YANIT:** VIF değerlerine bak. VIF > 10 ise ciddi bir çoklu doğrusal bağlantı sorunu vardır. Akademik olarak genellikle 5'in altı istenir.

## SORU 3: Aracılık (Mediation) Analizi
**Başlık:** Baron ve Kenny yöntemi hala geçerli mi?
**Kullanıcı:** Psikoloji_Tez | **Tarih:** 14 Ocak 2026
Danışmanım Process Macro kullanmamı istiyor, farkı nedir?
**✅ YANIT:** Baron-Kenny artık eskidi. Hayes'in **Process Macro**su (Bootstrap yöntemi) çok daha güçlü ve modern kabul ediliyor. Model 4 en yaygın aracılık modelidir.

## SORU 4: Moderasyon (Düzenleyici) Etkisi
**Başlık:** Etkileşim terimi (Interaction Term) nasıl oluşturulur?
**Kullanıcı:** Yonetim_Aras | **Tarih:** 13 Ocak 2026
Cinsiyetin eğitimin maaş üzerindeki etkisini değiştirdiğini nasıl test ederim?
**✅ YANIT:** Eğitim ve Cinsiyet değişkenlerini çarparak yeni bir değişken oluşturmalısın. Eğer bu çarpım terimi regresyonda anlamlı çıkarsa, moderasyon etkisi vardır.

## SORU 5: Kukla Değişken (Dummy Variable)
**Başlık:** Kategorik değişkenler regresyona nasıl girer?
**Kullanıcı:** Sosyal_Veri | **Tarih:** 12 Ocak 2026
Eğitim durumu (Lise, Lisans, Lisansüstü) değişkenini nasıl modele eklerim?
**✅ YANIT:** n-1 kuralını uygula. 3 kategorin varsa 2 adet kukla değişken oluşturmalısın. Bir kategoriyi "Referans" olarak dışarıda bırakmalısın.

---

# 🧠 KATEGORİ: YAPAY ZEKA & DERİN ÖĞRENME (5 İÇERİK)

## SORU 1: Kaggle Veri Setleri Güvenilir mi? ✅ ÇÖZÜLDÜ
**Başlık:** Tez çalışmamda Kaggle verisi kullanabilir miyim?
**Kullanıcı:** AI_Junior | **Tarih:** 16 Ocak 2026
Gerçek dünya verisi yerine Kaggle kullanmak akademik değerini düşürür mü?
**✅ YANIT:** Hayır, ancak verinin kaynağını (metadata) iyi açıklamalı ve "Secondary Data" olarak belirtmelisin. Çok popüler veri setleri (Titanic gibi) yerine daha spesifik olanları seç.

## SORU 2: Google Colab vs Local PC
**Başlık:** Derin öğrenme için RTX 3060 yeterli mi?
**Kullanıcı:** Donanim_Meraklisi | **Tarih:** 15 Ocak 2026
Kendi bilgisayarımda mı yoksa Colab bulutunda mı model eğitmeliyim?
**✅ YANIT:** 3060 giriş seviyesi için harika. Ancak çok katmanlı CNN veya Transformer eğiteceksen Google Colab'ın ücretsiz T4 GPU'su bazen daha hızlı olabilir.

## SORU 3: Overfitting (Aşırı Öğrenme) Nasıl Anlaşılır?
**Başlık:** Eğitim kaybı düşüyor ama test kaybı artıyor!
**Kullanıcı:** ModelEgitmeni | **Tarih:** 14 Ocak 2026
Modelim eğitim verisini ezberliyor, ne yapmalıyım?
**✅ YANIT:** Dropout katmanları ekle, öğrenme oranını (learning rate) düşür veya veri artırma (Data Augmentation) tekniklerini kullan.

## SORU 4: NLP'de BERT Modeli Nedir?
**Başlık:** Metin sınıflandırmada BERT neden bu kadar popüler?
**Kullanıcı:** Dil_Islemci | **Tarih:** 13 Ocak 2026
Word2Vec'ten farkı nedir?
**✅ YANIT:** BERT kelimenin "bağlamını" anlar. "Yüz" kelimesinin sayı mı yoksa çehre mi olduğunu sağındaki ve solundaki kelimelere bakarak (Bi-directional) çözer.

## SORU 5: Etik ve Yapay Zeka
**Başlık:** Yapay zeka modellerindeki taraflılık (Bias) sorunu
**Kullanıcı:** Etik_AI | **Tarih:** 12 Ocak 2026
Modelim neden hep belirli bir gruba karşı ayrımcı sonuçlar veriyor?
**✅ YANIT:** Eğitim verin yanlı (biased) olabilir. Eğer veride temsil edilmeyen gruplar varsa model bunu öğrenir. Verini dengelemen (balancing) şart.

---

# 📚 KATEGORİ: BİBLİYOMETRİK ANALİZLER (5 İÇERİK)

## SORU 1: VOSviewer vs Biblioshiny ✅ ÇÖZÜLDÜ
**Başlık:** Bibliyometrik görselleştirme için hangi araç daha iyi?
**Kullanıcı:** Literatur_Tarama | **Tarih:** 16 Ocak 2026
Görsel olarak hangisi makalelerde daha çok kabul görüyor?
**✅ YANIT:** VOSviewer ağ haritaları için standarttır. Biblioshiny (R-Bibliometrix) ise daha detaylı istatistiksel tablolar sunar. İkisini birden kullanmak en iyisidir.

## SORU 2: Veri Kaynağı: Scopus mu Web of Science mı?
**Başlık:** Hangi veri tabanı bibliyometride daha kapsayıcı?
**Kullanıcı:** Arastirmaci_X | **Tarih:** 15 Ocak 2026
İki veriyi birleştirebilir miyim?
**✅ YANIT:** Scopus genellikle daha fazla dergi içerir ama WoS daha prestijli kabul edilir. İkisini birleştirmek zordur (mükerrer kayıtlar yüzünden), genellikle tek bir tanesi seçilir.

## SORU 3: Ortak Atıf Analizi (Co-citation)
**Başlık:** Ortak atıf ile ortak yazarlık arasındaki fark nedir?
**Kullanıcı:** Bilim_Haritaci | **Tarih:** 14 Ocak 2026
Hangi analiz entelektüel yapıyı gösterir?
**✅ YANIT:** Co-citation analizi, iki makalenin aynı anda üçüncü bir makale tarafından kaynak gösterilmesidir. Bu, o alanın teorik temellerini ortaya çıkarır.

## SORU 4: H-İndeksi ve Diğer Metrikler
**Başlık:** Bir yazarın etkisini ölçmek için sadece H-indeksi yeterli mi?
**Kullanıcı:** AkademikKariyer | **Tarih:** 13 Ocak 2026
i10 indeksi ne işe yarar?
**✅ YANIT:** H-indeksi nicelik ve niteliği birleştirir ama yeni yazarlar için dezavantajlıdır. i10 indeksi ise Google Scholar'ın kullandığı, en az 10 atıf almış makale sayısını gösteren bir metriktir.

## SORU 5: Bibliyometrik Analiz Makalesi Yazımı
**Başlık:** Sadece bibliyometrik analiz ile Q1 dergide yayın yapılır mı?
**Kullanıcı:** YayinHedefi | **Tarih:** 12 Ocak 2026
Sadece grafik koymak yeterli mi?
**✅ YANIT:** Hayır. Grafiklerin ötesine geçip alanın "gelecek projeksiyonunu" yapmalı, boşlukları (research gaps) belirlemeli ve derinlemesine bir tartışma sunmalısın.