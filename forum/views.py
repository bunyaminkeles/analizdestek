from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib import messages
from django.http import JsonResponse
from .models import Section, Category, Topic, Post, Profile, ContactMessage, PrivateMessage
from .forms import RegisterForm, NewTopicForm, PostForm

# --- ANA SAYFA ---
def home(request):
    sections = Section.objects.all().order_by('order')
    return render(request, 'forum/home.html', {'sections': sections})

# --- KATEGORİ DETAY ---
def category_topics(request, slug):
    category = get_object_or_404(Category, slug=slug)
    topics = category.topics.annotate(replies_count=Count('posts')).order_by('-created_at')
    return render(request, 'forum/category_topics.html', {'category': category, 'topics': topics})

# --- KONU DETAY ---
def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    topic.views += 1
    topic.save()
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_detail', pk=pk)
    else:
        form = PostForm()

    return render(request, 'forum/topic_detail.html', {'topic': topic, 'form': form})

# --- KAYIT OLMA (Register) ---
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Profil oluşturma (Hata önleyici)
            if not hasattr(user, 'profile'):
                Profile.objects.create(user=user)
            
            login(request, user)
            messages.success(request, f"Aramıza hoş geldin, {user.username}!")
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'forum/register.html', {'form': form})

# --- PROFİL GÜNCELLEME (HATA BURADAYDI - DÜZELTİLDİ) ---
@login_required
def profile_edit(request):
    user = request.user
    
    if request.method == 'POST':
        # HTML'de name="email" kullandığınız için veriyi buradan manuel çekiyoruz
        new_email = request.POST.get('email')
        
        if new_email:
            # E-posta değişmiş mi ve başkası kullanıyor mu kontrolü
            if new_email != user.email and User.objects.filter(email=new_email).exists():
                messages.error(request, "Bu e-posta adresi kullanımda.")
            else:
                user.email = new_email
                user.save()
                messages.success(request, "Profil bilgileriniz başarıyla güncellendi.")
                return redirect('profile_edit') # Sayfayı yenile
        else:
            messages.error(request, "E-posta alanı boş bırakılamaz.")

    return render(request, 'forum/profile_edit.html', {'user': user})

# --- DİĞER SAYFALAR ---
def about(request):
    return render(request, 'forum/about.html')

def contact(request):
    if request.method == 'POST':
        # Contact modeliniz varsa burada kaydedebilirsiniz
        messages.success(request, "Mesajınız alındı.")
        return redirect('contact')
    return render(request, 'forum/contact.html')

def search_result(request):
    return render(request, 'forum/search_results.html')

@login_required
def profile_detail(request, username):
    profile_user = get_object_or_404(User, username=username)
    return render(request, 'forum/profile_detail.html', {'profile_user': profile_user})

@login_required
def new_topic(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.category = category
            topic.starter = request.user
            topic.save()
            # İlk mesajı oluştur
            Post.objects.create(topic=topic, message=form.cleaned_data['message'], created_by=request.user)
            return redirect('topic_detail', pk=topic.pk)
    else:
        form = NewTopicForm()
    return render(request, 'forum/new_topic.html', {'category': category, 'form': form})

@login_required
def summarize_topic(request, pk):
    # Geçici placeholder
    return redirect('topic_detail', pk=pk)

@login_required
def section_detail(request, pk):
    # Eğer section_detail sayfanız yoksa home'a yönlendirsin
    return redirect('home')

# forum/views.py dosyasının en üstündeki importlara PrivateMessage ekli değilse ekleyin:
# from .models import Section, Category, Topic, Post, Profile, ContactMessage, PrivateMessage 

# --- Gelen Kutusu (Inbox) Fonksiyonu ---
@login_required
def inbox(request):
    # Kullanıcıya gelen mesajları tarihe göre (en yeni en üstte) çek
    received_messages = PrivateMessage.objects.filter(receiver=request.user).order_by('-created_at')
    return render(request, 'forum/inbox.html', {'received_messages': received_messages})