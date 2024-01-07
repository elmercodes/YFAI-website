from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput


class CreateUserForm(UserCreationForm):
    
        class Meta:
            
            model = User
            fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
            

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
    
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)
    
    

