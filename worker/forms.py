from django import forms
from .models import Resume


class ResumeEditForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'age', 'specialization', 'info']
