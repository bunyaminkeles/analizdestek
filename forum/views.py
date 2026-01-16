from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum # ✅ Sum eklendi (Dashboard için şart)
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta

# Modellerin hepsi burada olmalı
from .models import Section, Category, Topic, Post, Profile, PrivateMessage, PostLike
from .forms import RegisterForm, NewTopicForm, PostForm
# Email servisi (Eğer dosya yoksa bu satırı yorum satırı yapın)
from .email_utils import send_topic_reply_notification, send_private_message_notification

# --- ANA SAYFA (DASHBOARD & LOBBY) ---
def home(request):
    """
    ANALIZUS Ana Ekranı:
    Hem bölüm kartlarını hem de dashboard istatistiklerini yükler.
    """
    sections = Section.objects.all().order_by('order')

    # 1. Dashboard İstatistikleri
    total_topics = Topic.objects.count()
    total_posts = Post.objects.count()
    total_users = User.objects.count()
    # Tüm konuların toplam görüntülenme sayısını toplar. Boşsa 0 döner.
    total_views = Topic.objects.aggregate(total=Sum('views'))['total'] or 0

    # 2. Son Tartışmalar (En yeni 5 konu)
    recent_topics = Topic.objects.select_related('starter', 'category').annotate(
        replies_count=Count('posts')
    ).order_by('-created_at')[:5]

    # 3. Popüler Konular (En çok görüntülenen 5 konu)
    popular_topics = Topic.objects.select_related('starter', 'category').annotate(
        replies_count=Count('posts')
    ).order_by('-views')[:5]

    # 4. Son Aktiviteler (Son atılan 10 mesaj)
    # DİKKAT: Post modelinde 'created_by' kullandığınız için burada da onu çağırıyoruz.
    recent_activities = Post.objects.select_related('created_by', 'topic').order_by('-created_at')[:10]

    context = {
        'sections': sections,
        # İstatistikler
        'total_topics': total_topics,
        'total_posts': total_posts,
        'total_users': total_users,
        'total_views': total_views,
        # Listeler
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
    # Sabitlenen konular (pinned) en üstte, sonra en yeni tarihli konular
    topics = category.topics.annotate(replies_count=Count('posts')).order_by('-is_pinned', '-created_at')
    return render(request, 'forum/category_topics.html', {'category': category, 'topics': topics})

# --- KONU DETAY VE CEVAP YAZMA ---
def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    
    # Görüntülenme sayısını artır (F5 yapınca artmasın diye session kontrolü eklenebilir ama şimdilik basit kalsın)
    topic.views += 1
    topic.save()

    posts = topic.posts.all().order_by('created_at')

    # Kullanıcının beğendiği postları belirle (Kalp ikonunu dolu göstermek için)
    user_liked_posts = []
    if request.user.is_authenticated:
        user_liked_posts = list(PostLike.objects.filter(
            user=request.user,
            post__in=posts
        ).values_list('post_id', flat=True))

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user # ✅ Post modelinizde author yerine created_by var
            post.save()

            # Email Bildirimi (Opsiyonel)
            try:
                send_topic_reply_notification(post, topic)
            except:
                pass # Mail gitmezse sistem çökmesin

            return redirect('topic_detail', pk=pk)
    else:
        form = PostForm()

    return render(request, 'forum/topic_detail.html', {
        'topic': topic,
        'posts': posts,
        'form': form,
        'user_liked_posts': user_liked_posts,
    })

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
            
            # Konuyla birlikte ilk mesajı da oluştur
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
            # ✅ Profil Sigortası: Eğer profil oluşmadıysa manuel oluştur
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
    # Profil yoksa oluştur (Güvenlik)
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)
        
    profile = user.profile
    
    if request.method == 'POST':
        # E-posta güncelleme
        new_email = request.POST.get('email')
        if new_email:
            user.email = new_email
            user.save()
        
        # Bildirim ayarları
        profile.email_on_reply = request.POST.get('email_on_reply') == 'on'
        profile.email_on_private_message = request.POST.get('email_on_private_message') == 'on'
        
        # Avatar ve Bio işlemleri form üzerinden geliyorsa buraya eklenebilir
        # Veya modelform kullanılabilir. Şimdilik temel ayarlar:
        profile.save()
        
        messages.success(request, "Profiliniz başarıyla güncellendi.")
        return redirect('profile_edit')
    
    return render(request, 'forum/profile_edit.html', {'user': user, 'profile': profile})

# --- GELEN KUTUSU (INBOX) ---
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
            
            # Email Bildirimi
            try:
                send_private_message_notification(request.user, receiver, message_content)
            except:
                pass

            messages.success(request, f"{receiver.username} adlı kullanıcıya mesajınız iletildi!")
            return redirect('profile_detail', username=username)
    
    return render(request, 'forum/send_message.html', {'receiver': receiver})

# --- PROFİL DETAY ---
def profile_detail(request, username):
    profile_user = get_object_or_404(User, username=username)
    # ✅ Hata Önleyici: Eski kullanıcıların profili yoksa anında oluştur
    if not hasattr(profile_user, 'profile'):
        Profile.objects.create(user=profile_user)
        
    return render(request, 'forum/profile_detail.html', {'profile_user': profile_user})

# --- STATİK SAYFALAR ---
def about(request):
    return render(request, 'forum/about.html')

def contact(request):
    return render(request, 'forum/contact.html')

def search_result(request):
    return render(request, 'forum/search_results.html')

def summarize_topic(request, pk):
    # İleride AI Entegrasyonu buraya gelecek
    return redirect('topic_detail', pk=pk)

# --- BEĞENİ (LIKE) SİSTEMİ ---
@login_required
def toggle_like(request, post_id):
    """Post beğenme/beğenmekten vazgeçme"""
    post = get_object_or_404(Post, pk=post_id)

    # Kullanıcı daha önce beğenmiş mi?
    like, created = PostLike.objects.get_or_create(user=request.user, post=post)

    if created:
        # Yeni like - Post üzerindeki sayacı artır
        post.likes += 1
        post.save()
        messages.success(request, "Yanıtı beğendiniz!")
    else:
        # Zaten like var - kaldır ve sayacı azalt
        like.delete()
        post.likes = max(0, post.likes - 1)
        post.save()
        messages.info(request, "Beğeniniz kaldırıldı.")

    return redirect('topic_detail', pk=post.topic.pk)