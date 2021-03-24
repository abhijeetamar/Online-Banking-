from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def form(request):
    if request.method =="POST":
        email=request.POST['email']
        message=request.POST['message']
        send_mail(
    ' ACCOUNT ACTIVATED',
    'your account is now activated.',
    'settings.EMAIL_HOST_USER',
    [''],#add the email id whom you want to send a mail to
    fail_silently=False,
)
    return render(request,'form.html')


