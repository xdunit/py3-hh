from django import forms
from .models import Vacancy


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'salary', 'description', 'is_relevant', 'email', 'contacts',
                  'candidate', 'review', 'category']
