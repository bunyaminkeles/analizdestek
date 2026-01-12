from django_ratelimit.decorators import ratelimit
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import JsonResponse
from django.contrib import messages

from .models import Section, Category, Topic, Post, Profile
from .forms import NewTopicForm, PostForm, RegisterForm # <--- RegisterForm eklendi

# AI Servisi importu
try:
    from .ai_service import AIAnalyst
except ImportError:
    AIAnalyst = None

def home(request):
    """Ana sayfa: Tüm bölümleri ve kategorileri listeler."""
    sections = Section.objects.all().prefetch_related('categories__topics')
    return render(request, 'forum/home.html', {'sections': sections})

def category_topics(request, slug):
    """Belirli bir kategoriye ait konuları listeler."""
    category = get_object_or_404(Category, slug=slug)
    topics = category.topics.annotate(replies_count=Count('posts')).order_by('-created_at')
    return render(request, 'forum/category_topics.html', {'category': category, 'topics': topics})

def topic_detail(request, pk):
    """Konu detaylarını ve mesajları gösterir."""
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

@login_required
def new_topic(request, slug):
    """Yeni bir konu başlığı ve ilk mesajı oluşturur."""
    category = get_object_or_404(Category, slug=slug)
    
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.category = category
            topic.starter = request.user
            topic.save()
            
            first_post = Post.objects.create(
                topic=topic,
                author=request.user,
                message=form.cleaned_data.get('message')
            )
            
            # AI Analiz Entegrasyonu
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

            return redirect('topic_detail', pk=topic.pk)
    else:
        form = NewTopicForm()
    
    return render(request, 'forum/new_topic.html', {'category': category, 'form': form})

def register(request):
    """Kayıt fonksiyonu: Hukuki onay ve profil oluşturma dahil."""
    if request.method == "POST":
        form = RegisterForm(request.POST) # <--- Özel formumuz
        if form.is_valid():
            user = form.save()
            # Profil kontrolü ve oluşturma
            if not hasattr(user, 'profile'):
                Profile.objects.create(user=user)
            
            login(request, user)
            messages.success(request, "Akademik veri üssüne hoş geldiniz! Kayıt başarıyla tamamlandı.")
            return redirect("home")
        else:
            messages.error(request, "Lütfen formu eksiksiz doldurun ve kullanım şartlarını kabul edin.")
    else:
        form = RegisterForm()
    return render(request, "forum/register.html", {"form": form})

def profile_detail(request, username):
    """Kullanıcı profili görüntüleme."""
    profile_user = get_object_or_404(User, username=username)
    return render(request, 'forum/profile_detail.html', {'profile_user': profile_user})

@ratelimit(key='ip', rate='5/m', block=True)
def search_result(request):
    """Gelişmiş arama fonksiyonu."""
    query = request.GET.get('q')
    results = []
    if query:
        results = Topic.objects.filter(
            Q(subject__icontains=query) | 
            Q(posts__message__icontains=query)
        ).distinct()
    
    return render(request, 'forum/search_results.html', {'query': query, 'results': results})

def summarize_topic(request, pk):
    """Konu tartışmasını özetleyen AI fonksiyonu."""
    topic = get_object_or_404(Topic, pk=pk)
    posts = topic.posts.all()
    
    if AIAnalyst:
        try:
            ai_engine = AIAnalyst()
            summary = ai_engine.summarize_discussion(topic.subject, posts)
        except Exception as e:
            summary = f"Özetleme sırasında bir hata oluştu: {e}"
    else:
        summary = "AI Servisi şu an ulaşılamaz durumda."
    
    return JsonResponse({'summary': summary})

def about(request):
    """Vizyon 2050 - Hakkımızda sayfası."""
    return render(request, 'forum/about.html')

def contact(request):
    """İletişim sayfası."""
    return render(request, 'forum/contact.html')