from django import forms
from .models import Profile
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['department','bio','location','birth_date']
        
class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['first_name','last_name','email']