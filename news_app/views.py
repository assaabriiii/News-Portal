from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import News, UserPreference
from .forms import SignUpForm, NewsPreferenceForm, CommentForm
from .utils.news_utils import get_trending_news
from .utils.user_utils import get_user_preferences
from django.http import JsonResponse
from django.template.loader import render_to_string

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('news_preference')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def news_preference(request):
    user_preferences = UserPreference.objects.filter(user=request.user)
    initial_preferences = [pref.news_class for pref in user_preferences]

    if request.method == 'POST':
        form = NewsPreferenceForm(request.POST)
        if form.is_valid():
            selected_preferences = form.cleaned_data['news_classes']
            
            # Delete old preferences
            UserPreference.objects.filter(user=request.user).delete()
            
            # Create new preferences with priority
            for priority, news_class in enumerate(selected_preferences):
                UserPreference.objects.create(
                    user=request.user,
                    news_class=news_class,
                    priority=priority
                )
            return redirect('dashboard')
    else:
        form = NewsPreferenceForm(initial={'news_classes': initial_preferences})
    
    return render(request, 'news_app/news_preference.html', {'form': form})

@login_required
def dashboard(request):
    user_preferences = get_user_preferences(request.user)
    if not user_preferences:
        return redirect('news_preference')
    
    # Create Q objects for each preferred category
    q_objects = Q()
    for preference in user_preferences:
        q_objects |= Q(newsClass=preference.news_class)
    
    # Get news from all preferred categories
    news_list = News.objects.filter(q_objects).order_by('-viewCounter')
    
    # Get trending news
    trending_news = get_trending_news(5)
    
    context = {
        'news_list': news_list,
        'trending_news': trending_news,
        'user_preferences': user_preferences
    }
    return render(request, 'news_app/dashboard.html', context)

    # NOTE
    # NEWS_CLASSES = [
    #     ('sports', 'Sports'),
    #     ('health', 'Health'),
    #     ('politics', 'Politics'),
    #     ('economics', 'Economics'),
    #     ('technology', 'Technology'),
    # ]

def technology_news(request):
    news_list = News.objects.filter(newsClass='technology').order_by('-viewCounter')
    context = {'news_list': news_list}
    return render(request, 'news_app/tech_news.html', context)

def sports_news(request):
    news_list = News.objects.filter(newsClass='sports').order_by('-viewCounter')
    context = {'news_list': news_list}
    return render(request, 'news_app/sports_news.html', context)

def health_news(request):
    news_list = News.objects.filter(newsClass='health').order_by('-viewCounter')
    context = {'news_list': news_list}
    return render(request, 'news_app/health_news.html', context)

def politics_news(request):
    news_list = News.objects.filter(newsClass='politics').order_by('-viewCounter')
    context = {'news_list': news_list}
    return render(request, 'news_app/politics_news.html', context)

def economics_news(request):
    news_list = News.objects.filter(newsClass='economics').order_by('-viewCounter')
    context = {'news_list': news_list}
    return render(request, 'news_app/economics_news.html', context)


class NewsList(LoginRequiredMixin, ListView):
    model = News
    template_name = 'news_app/news_list.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        user_preferences = get_user_preferences(self.request.user)
        if not user_preferences:
            return News.objects.none()
        
        q_objects = Q()
        for preference in user_preferences:
            q_objects |= Q(newsClass=preference.news_class)
        
        return News.objects.filter(q_objects).order_by('-viewCounter')

class NewsDetail(LoginRequiredMixin, DetailView):
    model = News
    template_name = 'news_app/news_detail.html'
    context_object_name = 'news'
    pk_url_kwarg = 'newsID'

    def get_object(self):
        obj = super().get_object()
        obj.viewCounter += 1
        obj.save()
        return obj

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    session_key = f'viewed_news_{pk}'
    if not request.session.get(session_key, False):
        news.viewCounter += 1
        news.save()
        request.session[session_key] = True

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.news = news
            comment.user = request.user
            comment.save()
            return redirect('news_detail', pk=news.pk)
    else:
        comment_form = CommentForm()
    return render(request, 'news_app/news_detail.html', {'news': news, 'comment_form': comment_form})

def fetch_comments(request, pk):
    news = get_object_or_404(News, pk=pk)
    comments_html = render_to_string('news_app/comments_section.html', {'news': news})
    return JsonResponse({'comments_html': comments_html})

def fetch_news_details(request, pk):
    news = get_object_or_404(News, pk=pk)
    news_html = render_to_string('news_app/news_details_section.html', {'news': news})
    return JsonResponse({'news_html': news_html})
