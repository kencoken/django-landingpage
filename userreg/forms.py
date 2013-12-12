from django import forms
from userreg.models import RegisteredUser

class RegisterUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        for f_name in self.fields:
            classes = self.fields[f_name].widget.attrs.get('class', '')
            if not classes:
                classes += ' '
            classes += 'form-control'
            self.fields[f_name].widget.attrs['class'] = classes
                    
    class Meta:
        model = RegisteredUser
        exclude = ('date','ip')
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Your email address'})
        }
