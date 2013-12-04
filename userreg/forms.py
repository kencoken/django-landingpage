from django import forms
from userreg.models import RegisteredUser

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = RegisteredUser
        exclude = ('date','ip')
