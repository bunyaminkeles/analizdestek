from django_ratelimit.decorators import ratelimit
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import threading

from .models import Section, Category, Topic, Post, Profile
from .forms import NewTopicForm, PostForm, RegisterForm

# AI Servisi importu
try:
    from .ai_service import AIAnalyst
except ImportError:
    AIAnalyst = None

# --- YARDIMCI FONKSİYONLAR ---
def send_notification_email(subject, message, recipient_list):
    """Mail gönderme işlemini arka planda yapar."""
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=recipient_list,
            fail_silently=True, 
        )
    except Exception as e:
        print(f"❌ Mail Hatası: {e}")

# --- VIEW FONKSİYONLARI ---

def home(request):
    """Lobby: 3 Ana Bölümü listeler."""
    sections = Section.objects.all().order_by('order')
    return render(request, 'forum/home.html', {'sections': sections})

def section_detail(request, pk):
    """Bölüm içi kategorileri listeler."""
    section = get_object_or_404(Section, pk=pk)
    categories = section.categories.all().prefetch_related('topics')
    return render(request, 'forum/section_detail.html', {
        'section': section, 
        'categories': categories
    })

def category_topics(request, slug):
    """Kategori içindeki konuları listeler."""
    category = get_object_or_404(Category, slug=slug)
    # replies_count için Post modeline bakıyoruz
    topics = category.topics.annotate(replies_count=Count('posts')).order_by('-created_at')
    return render(request, 'forum/category_topics.html', {'category': category, 'topics': topics})

def topic_detail(request, pk):
    """Konu detaylarını ve mesajları gösterir + BİLDİRİM ATAR"""
    topic = get_object_or_404(Topic, pk=pk)
    
    # Görüntülenme sayısını artır
    topic.views += 1
    topic.save()
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.author = request.user
            post.save()
            
            # BİLDİRİM SİSTEMİ
            if topic.starter.email and topic.starter != request.user:
                subject = f"🔔 Analizus: '{topic.subject}' konunuza cevap var!"
                message = f"Merhaba {topic.starter.username},\n\n'{topic.subject}' konunuza {request.user.username} tarafından cevap yazıldı.\n\nDetaylar: https://analizdestek-ai.onrender.com/topic/{topic.pk}/"
                
                threading.Thread(
                    target=send_notification_email, 
                    args=(subject, message, [topic.starter.email])
                ).start()

            # KRİTİK: Mesaj kaydedildikten sonra sayfayı tazele!
            return redirect('topic_detail', pk=pk)
    else:
        form = PostForm()

    # Mesajları taze çek
    posts = topic.posts.all().order_by('created_at')
    return render(request, 'forum/topic_detail.html', {'topic': topic, 'posts': posts, 'form': form})

@login_required
def new_topic(request, slug):
    """Yeni konu ve İLK MESAJI oluşturur."""
    category = get_object_or_404(Category, slug=slug)
    
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.category = category
            topic.starter = request.user
            topic.save()
            
            # İLK MESAJ KAYDI (Sizin görünmeniz için şart)
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
                    bot_user, _ = User.objects.get_or_create(username="AnalizBot")
                    Post.objects.create(topic=topic, author=bot_user, message=ai_response)
                except: pass

            return redirect('topic_detail', pk=topic.pk)
    else:
        form = NewTopicForm()
    return render(request, 'forum/new_topic.html', {'category': category, 'form': form})

# --- DİĞER FONKSİYONLAR (DÜZELTİLMİŞ) ---

@login_required
def profile_edit(request):
    user = request.user
    if request.method == 'POST':
        new_email = request.POST.get('email').strip()
        if User.objects.exclude(pk=user.pk).filter(email=new_email).exists():
            messages.error(request, "Bu e-posta adresi kullanımda.")
        else:
            user.email = new_email
            user.save()
            messages.success(request, "Profil güncellendi.")
            return redirect('profile_detail', username=user.username)
    return render(request, 'forum/profile_edit.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if not hasattr(user, 'profile'):
                Profile.objects.create(user=user)
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "forum/register.html", {"form": form})

def profile_detail(request, username):
    profile_user = get_object_or_404(User, username=username)
    return render(request, 'forum/profile_detail.html', {'profile_user': profile_user})

def search_result(request):
    query = request.GET.get('q')
    results = Topic.objects.filter(Q(subject__icontains=query) | Q(posts__message__icontains=query)).distinct() if query else []
    return render(request, 'forum/search_results.html', {'query': query, 'results': results})

def summarize_topic(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    # DÜZELTME: post.author.username (created_by değil)
    discussion_text = "\n".join([f"{post.author.username}: {post.message}" for post in topic.posts.all()])
    try:
        analyst = AIAnalyst()
        summary = analyst.summarize_discussion(discussion_text) if hasattr(analyst, 'summarize_discussion') else analyst.summarize(discussion_text)
        return JsonResponse({'summary': summary})
    except Exception as e:
        return JsonResponse({'summary': f"AI Hatası: {str(e)}"}, status=500)

def about(request):
    return render(request, 'forum/about.html')

def contact(request):
    if request.method == 'POST':
        name, email = request.POST.get('name'), request.POST.get('email')
        subject, message = request.POST.get('subject'), request.POST.get('message')
        if name and email and message:
            from .models import ContactMessage
            ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
            messages.success(request, "Mesajınız iletildi.")
            return redirect('contact')
    return render(request, 'forum/contact.html')

@login_required
def send_private_message(request, username):
    receiver = get_object_or_404(User, username=username)
    if request.method == 'POST':
        message_text = request.POST.get('message')
        if message_text:
            PrivateMessage.objects.create(
                sender=request.user,
                receiver=receiver,
                message=message_text
            )
            messages.success(request, f"{receiver.username} kullanıcısına mesajınız iletildi.")
            # Mail bildirimi tetiklenebilir (Daha önce kurduğumuz sistemle)
    return redirect('profile_detail', username=username)