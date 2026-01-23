from django import forms
from .models import Staff
from django.contrib.auth.forms import UserCreationForm

class CreateStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number']
        widgets = {
            'email': forms.EmailInput(attrs={'required': True}),
            }
