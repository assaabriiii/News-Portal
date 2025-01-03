from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.NewsList.as_view(), name='news_list'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Add dashboard URL
    path('signup/', views.signup, name='signup'),
    path('preference/', views.news_preference, name='news_preference'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('news/<int:pk>/fetch_comments/', views.fetch_comments, name='fetch_comments'),
    path('news/<int:pk>/fetch_news_details/', views.fetch_news_details, name='fetch_news_details'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]