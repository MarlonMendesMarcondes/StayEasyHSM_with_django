from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User, Profile

class UserRegisterForm(UserCreationForm):
    #first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Firstname', 'class': 'form-control w-50 m-2'}))
    #last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Lastname', 'class': 'form-control w-50 m-2'}))
    #username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Username', 'class': 'form-control w-50 m-2'}))
    #email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email', 'class': 'form-control w-50 m-2'}))
    #phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Phone Number', 'class': 'form-control w-50 m-2'}))
    #password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password', 'class': 'form-control w-50 m-2'}))
    #password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Your Password', 'class': 'form-control w-50 m-2'}))
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']