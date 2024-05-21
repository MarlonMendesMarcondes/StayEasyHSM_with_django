from django.shortcuts import render, redirect
from django.contrib import messages
from userauths.models import User, Profile
from userauths.forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout



def RegisterView(request):
    form = UserRegisterForm(request.POST)
    if request.user.is_authenticated:
        return redirect("hotel:index")
    
        
    
    if request.method == "POST":
        
        if form.is_valid():          

            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            profile = Profile.objects.get(user=request.user)
            profile.first_name = first_name
            profile.last_name = last_name
            profile.phone = phone
            profile.email = email
            messages.success(request, f"your register was successfully")
            user = authenticate(request,email=email,password=password)
            login(request, user)
            return redirect("hotel:index")      
        else:
            messages.error(request, f"your register was not successfully")   
    return render(request, "userauths/register.html", {'form': form})        
        

def LoginViewTemp(request):
    if request.user.is_authenticated:
        messages.warning(request, f" You are already logged in.")
        return redirect("hotel:index")
    pass

    if request.method == "POST":
        
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            user_query = User.objects.get(email=email)
            user_auth = authenticate(request, email=email, password=password)
            
            
            if user_query is not None:
                login(request, user_auth)
                messages.success(request, f"you are logged in")
                next_url = request.GET.get("next", "hotel:index")
                return redirect(next_url)
            
            else:
                messages.error(request, f"User or password dows not exist")
                return redirect("hotel:index")
        except:
            messages.error(request, f"User or password dows not exist")
    return render(request, "userauths/login.html")

def LogoutView(request):
    logout(request)
    messages.success(request, f"You have been logged out")
    return redirect("userauths:login")