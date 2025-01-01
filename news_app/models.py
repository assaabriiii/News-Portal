from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    NEWS_CLASSES = [
        ('sports', 'Sports'),
        ('health', 'Health'),
        ('politics', 'Politics'),
        ('economics', 'Economics'),
        ('technology', 'Technology'),
    ]
    
    newsID = models.AutoField(primary_key=True)
    newsTitle = models.CharField(max_length=200)
    newsBody = models.TextField()
    newsClass = models.CharField(max_length=20, choices=NEWS_CLASSES)
    viewCounter = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-viewCounter']
        verbose_name_plural = 'News'

    def __str__(self):
        return self.newsTitle

class UserPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news_class = models.CharField(
        max_length=20,
        choices=News.NEWS_CLASSES,
    )
    priority = models.IntegerField(default=0)

    class Meta:
        ordering = ['priority']
        unique_together = ['user', 'news_class']

    def __str__(self):
        return f"{self.user.username}'s preference: {self.news_class}"

class Comment(models.Model):
    news = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.news.newsTitle}"