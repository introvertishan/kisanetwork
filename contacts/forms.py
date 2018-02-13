from django import forms
from .models import *

class messages(forms.ModelForm):

    class Meta:
        model=Message
        fields='comment'