from django import forms 
from .models import Base

class TweetForm(forms.ModelForm):
    class Meta: 
        model = Base
        fields = ['text' , 'photo']