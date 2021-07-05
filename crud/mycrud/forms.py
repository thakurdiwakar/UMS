from django import forms
from django import forms
from django.forms import fields, widgets
from .models import User

class EmployeeRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','contact','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'contact':forms.NumberInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput( render_value=True, attrs={'class':'form-control'}),
        }