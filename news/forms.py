from django import forms
from .models import ArticleNew


class NewsUpdateForm(forms.ModelForm):
    class Meta:
        model = ArticleNew
        exclude = ['created_at', 'updated_at']


