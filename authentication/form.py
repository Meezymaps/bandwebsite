

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        #  form is associated with (User model)
        model = User
        
        # Define the fields to be displayed in the registration form
        fields = ['username', 'password1', 'password2']
