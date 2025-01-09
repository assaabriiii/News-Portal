from django.contrib import admin
from .models import News, UserPreference, Comment

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('newsID', 'newsTitle', 'newsClass', 'viewCounter')
    list_filter = ('newsClass',)
    search_fields = ('newsTitle', 'newsBody')

admin.site.site_header = 'News Portal Administration'
admin.site.site_title = 'News Portal Admin'
admin.site.index_title = 'Welcome to News Portal Admin'

