from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from Profile.models import BasicDetails
from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:signin")
    else:
        form = UserCreationForm()
    return render(request,"create_account.html", {"form": form})



def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("Profile:account_status")
    else:
        form = AuthenticationForm()
        return render(request,"sign_in.html", {"form": form})



def logout_view(request):
    #Logout the user if he hits the logout button
    logout(request)
    return redirect("accounts:signin")
