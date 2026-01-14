from django_ratelimit.decorators import ratelimit
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import JsonResponse
from django.contrib import messages
from django.http import JsonResponse

@login_required
def profile_edit(request):
    user = request.user
    
    if request.method == 'POST':
        new_email = request.POST.get('email').strip()
        
        # 1. Kontrol: Bu mail adresi başka bir kullanıcıya ait mi?
        if User.objects.exclude(pk=user.pk).filter(email=new_email).exists():
            messages.error(request, "Bu e-posta adresi başka bir hesap tarafından kullanılmaktadır.")
        else:
            # Kontrollerden geçtiyse kaydet
            user.email = new_email
            user.save()
            messages.success(request, "Profil bilgileriniz başarıyla güncellendi.")
            return redirect('profile_detail', username=user.username)
    
    return render(request, 'forum/profile_edit.html')

from .models import Section, Category, Topic, Post, Profile
from .forms import NewTopicForm, PostForm, RegisterForm # <--- RegisterForm eklendi

# AI Servisi importu
try:
    from .ai_service import AIAnalyst
except ImportError:
    AIAnalyst = None

def home(request):
    """
    YENİ ANA SAYFA (LOBBY):
    Sadece 3 Ana Bölümü (Section) kart olarak göstermek için çeker.
    Detayları çekmez, sadece başlıkları alır.
    """
    sections = Section.objects.all().order_by('order')
    return render(request, 'forum/home.html', {'sections': sections})

def section_detail(request, pk):
    """
    YENİ DETAY SAYFASI:
    Kullanıcı bir karta tıkladığında, o bölüme ait kategorileri (eski anasayfa gibi) listeler.
    """
    section = get_object_or_404(Section, pk=pk)
    # Sadece bu bölüme ait kategorileri ve içindeki konuları çekiyoruz
    categories = section.categories.all().prefetch_related('topics')
    
    return render(request, 'forum/section_detail.html', {
        'section': section, 
        'categories': categories
    })

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


# Kendi AI Analyst sınıfını import ettiğinden emin ol
# from .utils import AIAnalyst 

def summarize_topic(request, pk):
    topic = get_object_or_404(Topic, pk=pk) # Düzeltildi
    
    # Tartışma metnini topla
    discussion_text = "\n".join([f"{post.created_by.username}: {post.message}" for post in topic.posts.all()])
    
    try:
        analyst = AIAnalyst()
        # Sınıfındaki fonksiyon ismine göre burayı kontrol et (genelde 'summarize' olur)
        if hasattr(analyst, 'summarize_discussion'):
            summary = analyst.summarize_discussion(discussion_text)
        else:
            summary = analyst.summarize(discussion_text)
            
        return JsonResponse({'summary': summary})
    except Exception as e:
        return JsonResponse({'summary': f"AI Hatası: {str(e)}"}, status=500)
    
def about(request):
    """Vizyon 2050 - Hakkımızda sayfası."""
    return render(request, 'forum/about.html')

# Sadece contact fonksiyonunu bu şekilde değiştir
def contact(request):
    """İletişim sayfası: Formdan gelen mesajları kaydeder."""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_content = request.POST.get('message')

        if name and email and message_content:
            from .models import ContactMessage
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_content
            )
            messages.success(request, "Mesajınız başarıyla iletildi. Akademik ekibimiz sizinle iletişime geçecek.")
            return redirect('contact')
        else:
            messages.error(request, "Lütfen tüm zorunlu alanları doldurun.")
            
    return render(request, 'forum/contact.html')