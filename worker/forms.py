from django import forms
from .models import Resume


class ResumeEditForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'age', 'specialization', 'info', 'profile_photo', 'profile_photo']


class ResumeAdd(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'age', 'specialization', 'info', 'profile_photo']
