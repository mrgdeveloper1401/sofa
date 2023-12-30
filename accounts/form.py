from django import forms
from django.forms import ModelForm, Form
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import Users

class LoginForm(Form):
    mobile_phone = forms.CharField(max_length=11,
                                   label='شماره تلفن همراه')
    password = forms.CharField(min_length=8,
                               label=_('رمز عبور'),
                               widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))

class SignupForm(ModelForm):
    class Meta:
        model = Users
        fields = ('mobile_phone', 'password')