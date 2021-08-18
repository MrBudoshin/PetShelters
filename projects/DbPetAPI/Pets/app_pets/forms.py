from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from .models import Pet


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    mail = forms.CharField(max_length=30, required=False, help_text='Почта')
    phone = forms.CharField(max_length=30, required=False, help_text='Телефон')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']


class CreatePet(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'age', 'weight', 'special_signs']

