from django import forms
from .models import Vacancy
from .models import Company


class VacancyForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control my-input"}))

    class Meta:
        model = Vacancy
        fields = ['title', 'salary', 'description', 'is_relevant', 'email', 'contacts',
                  'candidate', 'review', 'category', 'experience', 'employment_type', 'skill_name']


class VacancyEditDj(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'salary', 'description', 'is_relevant', 'email', 'contacts',
                  'candidate', 'review', 'category', 'experience', 'employment_type', 'skill_name']


class CompanyAdd(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'workers',
                  'employees_num', 'is_hunting']


class CompanyEdit(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'workers',
                  'employees_num', 'is_hunting']
