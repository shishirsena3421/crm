from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput, EmailInput, DateTimeInput

from .models import Record, SERVICE_CHOICES, RIO_GRANDE_VALLEY_CITIES

# Register/Create a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'email': EmailInput(attrs={'type': 'email', 'placeholder': 'Email'}),
        }

# Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}))

# Create record
class CreateRecordForm(forms.ModelForm):
    city = forms.ChoiceField(choices=RIO_GRANDE_VALLEY_CITIES)
    service = forms.ChoiceField(choices=SERVICE_CHOICES)
    service_date = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}), input_formats=['%Y-%m-%dT%H:%M'])

    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'postal', 'service', 'service_date', 'Commentary']
        widgets = {
            'email': EmailInput(attrs={'type': 'email'}),
            'postal': TextInput(),
        }

# Update record
class UpdateRecordForm(forms.ModelForm):
    city = forms.ChoiceField(choices=RIO_GRANDE_VALLEY_CITIES)
    service = forms.ChoiceField(choices=SERVICE_CHOICES)
    service_date = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}), input_formats=['%Y-%m-%dT%H:%M'])

    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'postal', 'service', 'service_date', 'Commentary']
        widgets = {
            'email': EmailInput(attrs={'type': 'email'}),
            'postal': TextInput(),
        }
