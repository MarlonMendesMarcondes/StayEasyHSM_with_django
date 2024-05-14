from django.shortcuts import render, redirect
from django.contrib import messages
from userauths.models import User, Profile
from userauths.forms import UserRegisterForm
from django.contrib.auth import authenticate, login

def RegisterView(request):
    if request.user.is_authenticated:
        messages.warning(request, f" Hey {first_name} {last_name}, your already logged in.")
        return redirect("hotel:index")
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        form.save()
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        phone = form.cleaned_data.get('phone')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        
        user = authenticate(email=email,password = password)
        login(request, user)
        
        messages.success(request, f" Hey {first_name} {last_name}, your account has been created sucessfully.")
        
        profile = Profile.objects.get(user=request.user)
        profile.first_name = first_name
        profile.last_name = last_name
        profile.phone = phone
        profile.email = email
        profile.save()
        
        return redirect("")
    context = {
        "form":form
    }
    return render(request, "userauths/register.html", context)