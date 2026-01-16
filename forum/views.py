from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import Section, Category, Topic, Post, Profile, PrivateMessage
from .forms import RegisterForm, NewTopicForm, PostForm
from .email_utils import send_topic_reply_notification, send_private_message_notification  # ✅ YENİ

# --- ANA SAYFA ---
def home(request):
    sections = Section.objects.all().order_by('order')

    # Widget verileri
    # İstatistikler
    total_topics = Topic.objects.count()
    total_posts = Post.objects.count()
    total_users = User.objects.count()
    total_views = Topic.objects.aggregate(total=Sum('views'))['total'] or 0

    # Son tartışmalar (son 5 aktif konu)
    recent_topics = Topic.objects.select_related('starter', 'category').annotate(
        replies_count=Count('posts')
    ).order_by('-created_at')[:5]

    # Popüler konular (en çok görüntülenen 5 konu)
    popular_topics = Topic.objects.select_related('starter', 'category').annotate(
        replies_count=Count('posts')
    ).order_by('-views')[:5]

    # Son aktiviteler (son 10 post)
    recent_activities = Post.objects.select_related('created_by', 'topic').order_by('-created_at')[:10]

    context = {
        'sections': sections,
        # İstatistikler
        'total_topics': total_topics,
        'total_posts': total_posts,
        'total_users': total_users,
        'total_views': total_views,
        # Widgetlar
        'recent_topics': recent_topics,
        'popular_topics': popular_topics,
        'recent_activities': recent_activities,
    }
    return render(request, 'forum/home.html', context)

# --- BÖLÜM DETAY ---
def section_detail(request, pk):
    section = get_object_or_404(Section, pk=pk)
    categories = section.categories.all()
    return render(request, 'forum/section_detail.html', {'section': section, 'categories': categories})

# --- KATEGORİ VE KONULAR ---
def category_topics(request, slug):
    category = get_object_or_404(Category, slug=slug)
    topics = category.topics.annotate(replies_count=Count('posts')).order_by('-created_at')
    return render(request, 'forum/category_topics.html', {'category': category, 'topics': topics})

# --- KONU DETAY VE CEVAP YAZMA ---
def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    topic.views += 1
    topic.save()
    
    posts = topic.posts.all().order_by('created_at')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            
            # ✅ EMAIL BİLDİRİMİ GÖNDER
            send_topic_reply_notification(post, topic)
            
            return redirect('topic_detail', pk=pk)
    else:
        form = PostForm()

    return render(request, 'forum/topic_detail.html', {'topic': topic, 'posts': posts, 'form': form})

# --- YENİ KONU AÇMA ---
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
            Post.objects.create(
                topic=topic,
                message=form.cleaned_data['message'],
                created_by=request.user
            )
            return redirect('topic_detail', pk=topic.pk)
    else:
        form = NewTopicForm()
    return render(request, 'forum/new_topic.html', {'category': category, 'form': form})

# --- KAYIT ---
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if not hasattr(user, 'profile'):
                Profile.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'forum/register.html', {'form': form})

# --- PROFİL DÜZENLE ---
@login_required
def profile_edit(request):
    user = request.user
    profile = user.profile
    
    if request.method == 'POST':
        new_email = request.POST.get('email')
        if new_email:
            user.email = new_email
            user.save()
        
        # ✅ Email tercihlerini kaydet
        profile.email_on_reply = request.POST.get('email_on_reply') == 'on'
        profile.email_on_private_message = request.POST.get('email_on_private_message') == 'on'
        profile.save()
        
        messages.success(request, "Profil güncellendi.")
        return redirect('profile_edit')
    
    return render(request, 'forum/profile_edit.html', {'user': user, 'profile': profile})

# --- GELEN KUTUSU ---
@login_required
def inbox(request):
    received_messages = PrivateMessage.objects.filter(receiver=request.user).order_by('-created_at')
    return render(request, 'forum/inbox.html', {'received_messages': received_messages})

# --- ÖZEL MESAJ GÖNDER ---
@login_required
def send_message(request, username):
    receiver = get_object_or_404(User, username=username)
    
    if request.method == 'POST':
        message_content = request.POST.get('message')
        if message_content:
            PrivateMessage.objects.create(
                sender=request.user,
                receiver=receiver,
                message=message_content
            )
            
            # ✅ EMAIL BİLDİRİMİ GÖNDER
            send_private_message_notification(request.user, receiver, message_content)
            
            messages.success(request, f"{receiver.username} kullanıcısına mesajınız gönderildi!")
            return redirect('profile_detail', username=username)
    
    return render(request, 'forum/send_message.html', {'receiver': receiver})

# --- PROFİL DETAY ---
def profile_detail(request, username):
    profile_user = get_object_or_404(User, username=username)
    return render(request, 'forum/profile_detail.html', {'profile_user': profile_user})

# --- DİĞER ---
def about(request):
    return render(request, 'forum/about.html')

def contact(request):
    return render(request, 'forum/contact.html')

def search_result(request):
    return render(request, 'forum/search_results.html')

def summarize_topic(request, pk):
    return redirect('topic_detail', pk=pk)
