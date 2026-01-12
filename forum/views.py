from django_ratelimit.decorators import ratelimit
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count, Q
from django.http import JsonResponse  # <--- BU EKLENDİ

from .models import Section, Category, Topic, Post, Profile
from .forms import NewTopicForm, PostForm 

# AI Servisi importu
try:
    from .ai_service import AIAnalyst
except ImportError:
    AIAnalyst = None

def home(request):
    sections = Section.objects.all().prefetch_related('categories__topics')
    return render(request, 'forum/home.html', {'sections': sections})

def category_topics(request, slug):
    category = get_object_or_404(Category, slug=slug)
    topics = category.topics.annotate(replies_count=Count('posts')).order_by('-created_at')
    return render(request, 'forum/category_topics.html', {'category': category, 'topics': topics})

def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    
    # Görüntülenme sayısını artır
    topic.views += 1
    topic.save()
    
    posts = topic.posts.all().order_by('created_at')
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.author = request.user
            post.save()
            return redirect('topic_detail', pk=pk)
    else:
        form = PostForm()

    return render(request, 'forum/topic_detail.html', {'topic': topic, 'posts': posts, 'form': form})

# Arama fonksiyonuna sınır: Dakikada en fazla 5 arama
@ratelimit(key='ip', rate='5/m', block=True)
def search_result(request):
    # ... mevcut kodlar ...
    return render(request, 'forum/search_results.html', {'query': query, 'results': results})

@login_required
def new_topic(request, slug):
    category = get_object_or_404(Category, slug=slug)
    
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            # 1. Konuyu Kaydet
            topic = form.save(commit=False)
            topic.category = category
            topic.starter = request.user
            topic.save()
            
            # 2. İlk Mesajı Kaydet
            first_post = Post.objects.create(
                topic=topic,
                author=request.user,
                message=form.cleaned_data.get('message')
            )
            
            # --- AI ANALİZ ENTEGRASYONU ---
            if AIAnalyst:
                try:
                    ai_engine = AIAnalyst()
                    ai_response = ai_engine.generate_response(topic.subject, first_post.message)
                    
                    bot_user, created = User.objects.get_or_create(username="AnalizBot")
                    if created:
                        bot_user.set_unusable_password()
                        if not hasattr(bot_user, 'profile'):
                             Profile.objects.create(user=bot_user, title="Yapay Zeka Asistanı", account_type="Expert")
                        bot_user.save()

                    Post.objects.create(topic=topic, author=bot_user, message=ai_response)
                except Exception as e:
                    print(f"AI Bot Hatası: {e}")
            # ------------------------------

            return redirect('topic_detail', pk=topic.pk)
    else:
        form = NewTopicForm()
    
    return render(request, 'forum/new_topic.html', {'category': category, 'form': form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if not hasattr(user, 'profile'):
                Profile.objects.create(user=user)
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "forum/register.html", {"form": form})

def profile_detail(request, username):
    profile_user = get_object_or_404(User, username=username)
    return render(request, 'forum/profile_detail.html', {'profile_user': profile_user})

def search_result(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Topic.objects.filter(
            Q(subject__icontains=query) | 
            Q(posts__message__icontains=query)
        ).distinct()
    
    return render(request, 'forum/search_results.html', {'query': query, 'results': results})

# --- EKSİK OLAN FONKSİYON BURAYA EKLENDİ ---
def summarize_topic(request, pk):
    """
    Belirli bir konuyu AI servisine gönderir ve özeti JSON olarak döner.
    """
    topic = get_object_or_404(Topic, pk=pk)
    posts = topic.posts.all()
    
    if AIAnalyst:
        ai_engine = AIAnalyst()
        summary = ai_engine.summarize_discussion(topic.subject, posts)
    else:
        summary = "AI Servisi aktif değil veya yüklenemedi."
    
    return JsonResponse({'summary': summary})