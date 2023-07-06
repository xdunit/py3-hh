from django import forms
from .models import Vacancy
from .models import Company


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'salary', 'description', 'is_relevant', 'email', 'contacts',
                  'candidate', 'review', 'category']


class VacancyEditDj(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'salary', 'description', 'is_relevant', 'email', 'contacts',
                  'candidate', 'review', 'category']


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
