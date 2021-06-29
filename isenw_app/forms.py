# forms.py
from django import forms
from .models import *


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields="__all__"