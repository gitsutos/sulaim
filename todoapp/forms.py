from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
#from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    re_Type_Password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ['username','password','email']
