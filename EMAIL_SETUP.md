# Email Bildirimleri Kurulumu (SendGrid)

## 1. SendGrid Hesabı Oluşturma

1. https://signup.sendgrid.com/ adresinden ücretsiz hesap açın
2. Email adresinizi doğrulayın

## 2. API Key Oluşturma

1. https://app.sendgrid.com/settings/api_keys adresine gidin
2. "Create API Key" butonuna tıklayın
3. İsim verin (örn: "AnalizDestek Production")
4. **Full Access** seçin
5. "Create & View" tıklayın
6. **API Key'i kopyalayın** (tekrar göremezsiniz!)
   - Format: `SG.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

## 3. Single Sender Verification (Önemli!)

SendGrid free tier için gönderici email adresini doğrulamanız gerekir:

1. https://app.sendgrid.com/settings/sender_auth/senders adresine gidin
2. "Create New Sender" tıklayın
3. Bilgileri doldurun:
   - **From Email Address**: Kendi email adresiniz (örn: `bkeles74@gmail.com`)
   - **From Name**: `AnalizDestek`
   - **Reply To**: Aynı email
   - Diğer alanları doldurun
4. "Save" tıklayın
5. **Gelen verification emaili onaylayın**
6. ✅ Doğrulandıktan sonra bu adresten email gönderebilirsiniz

## 4. Render Environment Variables

Render Dashboard → Your Service → Environment sekmesine gidin ve ekleyin:

```
SENDGRID_API_KEY=SG.your_actual_api_key_here
DEFAULT_FROM_EMAIL=YourName <youremail@example.com>
```

⚠️ **Önemli**: `DEFAULT_FROM_EMAIL` Single Sender Verification'da doğruladığınız email ile aynı olmalı!

## 5. Lokal Test (Opsiyonel)

Lokalde test etmek için `.env` dosyası oluşturun:

```bash
cp .env.example .env
nano .env
```

`.env` içeriği:
```
SENDGRID_API_KEY=SG.your_actual_api_key_here
DEFAULT_FROM_EMAIL=YourName <youremail@example.com>
```

## 6. Test

1. Render'da deploy edin
2. İki farklı kullanıcıyla test edin:
   - Kullanıcı A: Konu açsın
   - Kullanıcı B: Konuya cevap yazsın
   - Kullanıcı A'nın emailine bildirim gitmeli

3. Özel mesaj testi:
   - Kullanıcı A: Kullanıcı B'ye özel mesaj göndersin
   - Kullanıcı B'nin emailine bildirim gitmeli

## Sorun Giderme

### Email gitmiyor:

1. **Render loglarını kontrol edin:**
   ```
   💌 Özel mesaj email kontrolü: teğmen -> bunyamin
   📧 Email gönderme başlıyor: ['email@example.com']
   📤 SMTP bağlantısı kuruluyor...
   ✅ Email gönderildi: ['email@example.com']
   ```

2. **Hata mesajları:**
   - `❌ SENDGRID_API_KEY TANIMLI DEĞİL!` → Render'da env variable ekleyin
   - `❌ Email gönderim hatası: 401 Unauthorized` → API key yanlış
   - `❌ Email gönderim hatası: 403 Forbidden` → Single Sender Verification yapılmamış

3. **SendGrid Dashboard:**
   - https://app.sendgrid.com/email_activity
   - Son gönderimler ve hataları görebilirsiniz

## Limitler

SendGrid Free Tier:
- ✅ 100 email/gün
- ✅ Single Sender Verification (1 email adresi)
- ❌ Custom domain (ücretli planda)

İhtiyacınız varsa ücretli plana geçebilirsiniz.
