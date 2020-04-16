from django import forms
from django.contrib.auth.models import User
from basicapp.models import UserProfileInfo

class UserForm(forms.ModelForm):
    class Meta():
        model=User
        fields=('username','password','email')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')
   