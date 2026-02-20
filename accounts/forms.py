from django import forms
from .models import Staff

class CreateStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['first_name', 'other_names', 'last_name', 'username', 'email', 'password', 'phone_number']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.force_password_change = True
        if commit:
            user.save()
        return user
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)