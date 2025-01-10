from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import News, UserPreference, Comment

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = "Your username must be 18 characters or fewer"

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) >= 18:
            raise forms.ValidationError("Username must be less than 18 characters")
        return username

class NewsPreferenceForm(forms.Form):
    news_classes = forms.MultipleChoiceField(
        choices=News.NEWS_CLASSES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=False,
        label='Select your preferred news categories:'
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)
        widgets = {
            'comment_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
