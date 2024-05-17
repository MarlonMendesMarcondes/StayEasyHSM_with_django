from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User, Profile

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Firstname', 'class': ''}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Lastname', 'class': ''}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Username', 'class': ''}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email', 'class': ''}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Phone Number', 'class': ''}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password', 'class': ''}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Your Password', 'class': ''}))
    class Meta:
        model = User
        fields = ['first_name','last_name', 'phone' ,'username','email', 'password1', 'password2']