from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#A register form that save field is_active as False
class RegisterForm(UserCreationForm):
    email = forms.EmailField(label=_("E-mail"))
    first_name = forms.CharField(label=_("First Name"))
    last_name = forms.CharField(label=_("Last Name"))
    is_active = forms.BooleanField(required=False, initial=False, label=_("Active"), widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2','is_active')

        def save(self, commit=True):
            user = super(UserCreationForm, self).save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            user.is_active = self.cleaned_data['is_active']
            if commit:
                user.save()
            return user