from ..models import UserPreference

def get_user_preferences(user):
    """
    Get user's news preferences ordered by priority
    """
    return UserPreference.objects.filter(user=user).order_by('priority')

def set_user_preferences(user, news_classes):
    """
    Set or update user's news preferences
    """
    # Delete existing preferences
    UserPreference.objects.filter(user=user).delete()
    
    # Create new preferences with priority
    preferences = []
    for priority, news_class in enumerate(news_classes):
        preference = UserPreference.objects.create(
            user=user,
            news_class=news_class,
            priority=priority
        )
        preferences.append(preference)
    return preferences