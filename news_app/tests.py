from django.test import TestCase
from django.contrib.auth.models import User
from .models import News, UserPreference


class NewsModelTests(TestCase):
    def setUp(self):
        self.news = News.objects.create(
            newsTitle="Test News",
            newsBody="Test Body",
            newsClass="sports",
            viewCounter=0
        )

    def test_view_counter_increment(self):
        initial_views = self.news.viewCounter
        self.news.viewCounter += 1
        self.news.save()
        self.assertEqual(self.news.viewCounter, initial_views + 1)


class UserPreferenceTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_user_preference_creation(self):
        preference = UserPreference.objects.create(
            user=self.user,
            preferred_news_class='sports'
        )
        self.assertEqual(preference.user, self.user)
        self.assertEqual(preference.preferred_news_class, 'sports')