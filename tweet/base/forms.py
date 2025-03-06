from django import forms 
from .models import Base
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta: 
        model = Base
        fields = ['text' , 'photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta :
        model = User
        fields = ('username' , 'email' , 'password1' , 'password2')