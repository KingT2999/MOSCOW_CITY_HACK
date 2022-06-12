from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Volunteer


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1']

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = '__all__'
        exclude = ['user']