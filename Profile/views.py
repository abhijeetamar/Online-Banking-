from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from Profile.models import Status
import random
import sys
# Create your views here.
def randomGen():
    return int(random.uniform(100000000000, 999999999999))

def index(request):
    try:
        curr_user=Status.objects.get(user_name=request.user)
    except:
        curr_user=Status()
        curr_user.account_number=randomGen()
        curr_user.balance=0
        curr_user.user_name=request.user
        curr_user.save()
    return render(request,'Profile.html',{"curr_user":curr_user})
def edit_detail(request):
    #post actions for BasicDetailsForms
    if request.method=="POST":
        try:
            curr_user=models.BasicDetails.objects.get(user_name=request.user)
            form=forms.BasicDetailsForm(request.POST,instance=curr_user)
            if form.is_valid():
                form.save
        except:
            form=forms.BasicDetailsForm(request.POST)
            if form.is_valid():
                form=form.save(commit=False)
                form.user_name=request.user
                form.save()


        #post action for present location
        try:
            curr_user=models.PresentLocation.objects.get(user_name=request.user)
            form=forms.PresentLocationForm(request.POST,instance=curr_user)
            if form.is_valid():
                form.save()
        except:
            form=forms.PresentLocationForm(request.POST)
            if form.is_valid():
                form=form.save(commit=False)
                form.user_name=request.user
                form.save()

        #post action for password change
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Your password was successfully changed')
            return redirect('edit_detail.html')
        else:
            messages.error(request,'Please correct the error')
        return redirect('edit_detail.html')
    else:
        try:
            curr_user=models.BasicDetails.objects.get(user_name=request.user)
            form1=forms.BasicDetailsForm(instance=curr_user)
        except:
            form1=forms.BasicDetailsForm()
        try:
            curr_user=models.PresentLocation.objects.get(user_name=request.user)
            form2=forms.PresentLocationForm(instance=curr_user)
        except:
            form2=forms.PresentLocationForm()
        #change password
        dici={"form1":form1,"form2":form2,"form3":form3}
        return render(request,'edit_detail.html',dici)


def money_transfer(request):
    return render(request,'money_transfer.html')


def loan(request):
    return render(request, "loans.html")


def ewallet(request):
    return render(request, "eWallet.html")


def online_pay(request):
    return render(request, "online_payment.html")


def settings(request):
    return render(request, "settings.html")


def delete_account(request):
    return render(request,'Delete_account.html')


class Customer:

    bankname="SBI"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print("Balance after Deposit:",self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print("insufficient Funds..cannot Perform this operations")
            sys.exit()
        self.balance=self.balance-amt
        print('Balance after withdraw"',self.balance)
print('Welcome to',Customer.bankname)
name=input("Enter your name:")
c=Customer(name)






