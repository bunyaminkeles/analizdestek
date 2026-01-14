from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Topic, Post
from django.utils.safestring import mark_safe

# --- 1. KAYIT FORMU ---
class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        label="E-Posta Adresi",
        help_text="Geçerli bir e-posta adresi giriniz."
    )
    
    # Checkbox (HTML'de manuel olsa da burada tanımlı olması veri doğrulaması için iyidir)
    terms_confirmed = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label="Kullanım Şartları",
        error_messages={'required': 'Kayıt olmak için şartları kabul etmelisiniz.'}
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email") # Şifre alanları (password1/2) otomatiktir.

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu e-posta adresi sistemde zaten kayıtlı.")
        return email

# --- 2. YENİ KONU FORMU ---
class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 10, 'placeholder': 'İçeriği buraya yazın...'}),
        label="Mesaj",
        max_length=4000
    )
    class Meta:
        model = Topic
        fields = ['subject']
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': 'Konu Başlığı'}),
        }

# --- 3. CEVAP FORMU ---
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Cevabınızı yazın...'}),
        }