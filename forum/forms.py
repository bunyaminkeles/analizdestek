from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Topic, Post

# 1. Kayıt Formu (Hukuki Onay Mekanizmalı)
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="E-posta Adresi")
    
    # Bu alan işaretlenmezse form kayıt yapmaz
    terms_confirmed = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label="Kullanım Şartlarını ve Etik Beyanı kabul ediyorum."
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

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