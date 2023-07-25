from django import forms
from .models import Recruiter


class RecruiterEditForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        fields = ['city', 'country', 'payment_for_found', 'bonus_percent']
