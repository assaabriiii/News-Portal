from django.contrib import admin
from .models import News, UserPreference, Comment

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('newsID', 'newsTitle', 'newsClass', 'viewCounter')
    list_filter = ('newsClass',)
    search_fields = ('newsTitle', 'newsBody')

@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'news_class')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('news', 'user', 'created_at')
    search_fields = ('comment_text',)
