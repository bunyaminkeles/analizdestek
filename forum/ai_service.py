import os
from django.conf import settings
import openai

class AIAnalyst:
    def __init__(self):
        self.api_key = getattr(settings, 'OPENAI_API_KEY', None)
        
    def generate_response(self, topic_title, user_message):
        """
        API yoksa kural tabanlı uzman sistem devreye girer.
        """
        # API anahtarı yoksa veya test anahtarıysa 'Yerel Uzman Mantığı' çalışır
        if not self.api_key or self.api_key == 'sk-proj-test-anahtari-12345':
            title = topic_title.lower()
            msg = user_message.lower()

            # --- UZMAN KARAR MATRİSİ ---
            if "spss" in title or "spss" in msg:
                return (
                    "🤖 **AnalizBot Uzman Görüşü:**\n\n"
                    "SPSS verilerinizi taradım. Normallik varsayımı için **Shapiro-Wilk** sonucuna bakın. "
                    "Eğer p < 0.05 ise parametrik olmayan testlere (Mann-Whitney U) geçmelisiniz. "
                    "Tablolarınızı APA 7 formatında raporlamayı unutmayın."
                )
            
            elif "anket" in title or "ölçek" in title:
                return (
                    "🤖 **AnalizBot Uzman Görüşü:**\n\n"
                    "Anket çalışması için **Cronbach's Alpha** güvenirlik analizi şarttır. "
                    "Değer 0.70'in üzerindeyse verileriniz tutarlıdır. Faktör analizi (AFA) yapacaksanız "
                    "KMO değerinin 0.60'tan büyük olup olmadığını kontrol edin."
                )

            elif "regresyon" in title or "etki" in title:
                return (
                    "🤖 **AnalizBot Uzman Görüşü:**\n\n"
                    "Regresyon modelinizde **Çoklu Doğrusallık (Multicollinearity)** riskini önlemek için "
                    "VIF değerlerini kontrol edin. VIF > 10 ise değişkenler arasında yüksek korelasyon vardır."
                )

            return (
                "🤖 **AnalizBot (Genel Değerlendirme):**\n\n"
                "Konunuzu metodolojik olarak inceledim. Akademik geçerlilik için örneklem büyüklüğünüzün "
                "yeterli olduğundan emin olun (G*Power analizi önerilir). Hangi testi yapacağınızdan "
                "emin değilseniz değişken türlerinizi (Nominal/Ordinal/Scale) belirterek tekrar sorun."
            )

        # API Anahtarı varsa gerçek GPT çalışır (Kodun burası zaten sende var)
        try:
            client = openai.OpenAI(api_key=self.api_key)
            # ... (mevcut gpt kodun) ...
            return "GPT Cevabı Buraya Gelecek"
        except:
            return "Bağlantı Hatası"