from django.contrib.auth.models import User
from django.db.models import signals
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from django.core.mail import send_mail

@receiver(post_save,sender=User)
def my_callback(sender,created,instance, **kwargs):
    if created:
        print("user created")

    else:
        print("no user created")

#signal used for is_active=False to is_active=True
@receiver(pre_save, sender=User, dispatch_uid='active')
def active(sender, instance, **kwargs):
    if instance.is_active :
        # subject = 'Active account'
        # message = ' your account is now active'
        # from_email = settings.EMAIL_HOST_USER
        # send_mail(subject, message, from_email, [instance.email], fail_silently=False)
        # print("EMAIL SENT")
        send_mail(
            'Active account',#subject
         ' your account is now active you can login now',#Message
         'settings.EMAIL_HOST_USER',#thezerocoder@gmail.com
         ['abhijeetamaranalogit@gmail.com'],#recipient email id
           fail_silently=False,
          
        )
        print('Email Sent')

# #signal to send an email to the admin when a user creates a new account
# @receiver(post_save, sender=User, dispatch_uid='register')
# def register(sender, instance, **kwargs):
#     if kwargs.get('created', False):
#         subject = 'Verificatión of the account'
#         mesagge = 'here goes your message to the admin'
#         from_email = settings.EMAIL_HOST_USER
#         send_mail(subject, mesagge, from_email, [from_email], fail_silently=False)

