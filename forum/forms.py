from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Topic, Post
from django.utils.safestring import mark_safe # <--- BU SATIRI EKLEYİN

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    # E-posta alanını zorunlu hale getiriyoruz
    email = forms.EmailField(
        required=True, 
        label="E-Posta Adresi",
        widget=forms.EmailInput(attrs={'placeholder': 'örnek@üniversite.edu.tr'})
    )

    class Meta:
        model = User
        fields = ('username', 'email') # Şifre alanları UserCreationForm'dan otomatik gelir

    # İŞTE UÇAN KONTROL BURADA:
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Veritabanında bu mail var mı diye bakıyoruz
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu e-posta adresi başka bir kullanıcı tarafından alınmış.")
        return email

# 2. Yeni Konu Açma Formu
class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 10, 'placeholder': 'Akademik analiz veya tartışma içeriğini buraya yazın...'}),
        label="Mesaj İçeriği",
        max_length=4000 # AI maliyetini korumak için sınır
    )
    
    class Meta:
        model = Topic
        fields = ['subject']
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': 'Analiz Başlığı (Örn: SPSS Regresyon Hatası)'}),
        }

# 3. Cevap Yazma Formu
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Bilimsel katkınızı veya cevabınızı buraya yazın...'}),
        }