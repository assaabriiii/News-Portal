from django.db.models import F
from ..models import News

def increment_view_counter(news_id):
    """
    Increment the view counter for a specific news article
    """
    News.objects.filter(newsID=news_id).update(viewCounter=F('viewCounter') + 1)

def get_news_by_category(category):
    """
    Get all news articles for a specific category, ordered by view count
    """
    return News.objects.filter(newsClass=category).order_by('-viewCounter')

def get_trending_news(limit=5):
    """
    Get trending news articles based on view count
    """
    return News.objects.all().order_by('-viewCounter')[:limit]