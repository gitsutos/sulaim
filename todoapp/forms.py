from django import forms
#from django.forms import widgets
#from django.forms.widgets import PasswordInput, TextInput, Widget
from django.contrib.auth.models import User

class UserSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username','password','email','first_name','last_name')