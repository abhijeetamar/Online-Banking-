from django import forms
from . import models

class BasicDetailsForm (forms.ModelForm):
  
    class Meta:
        model = models.BasicDetails
        fields = ["name", "sex", "DOB", "annual_income", "email", "mobile", "occupation"]


class PresentLocationForm (forms.ModelForm):
    class Meta:
        model = models.PresentLocation
        fields = ["country", "state", "city", "street", "pincode"]