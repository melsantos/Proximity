from django import forms
from django.contrib.auth import (    authenticate, get_user_model, password_validation,)
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.hashers import ( UNUSABLE_PASSWORD_PREFIX, identify_hasher,)
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.text import capfirst
from django.utils.translation import gettext as _
from django.utils.translation import gettext, gettext_lazy as _
from pages.models import Document, Profile
import unicodedata

class CustomUserCreationForm(UserCreationForm):
    # User fields
    username = forms.CharField(label='Username')
    firstname = forms.CharField(label='First Name')
    lastname = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    # Profile fields
    age = forms.IntegerField(label='Age')

    class Meta:
        model = User
        fields = ('username', 'firstname', 'lastname', 'age', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.Meta.fields:
            actualField = self.fields.get(field)
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                # 'placeholder': actualField.label
            })

    # Checks if username is taken
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError(_("Username is taken."), code='usernameError' )
        return username

    # Checks if an email is already associated with an account
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError(_("Email is already linked to an account."), code='emailError')
        return email

    # Checks if passwords match
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Password do not match."), code='passwordError')

        return password2

    # Checks if age is over 18
    def clean_age(self):
        age = self.cleaned_data.get('age')

        if age is None:
            raise ValidationError(_("Age is required."), code='ageError')

        if age < 18:
            raise ValidationError(_("You must be over 18."), code='ageError')

        return age

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
        )
        user.first_name = self.cleaned_data['firstname']
        user.last_name = self.cleaned_data['lastname']
        if commit:
            user.save()
        return user

class CustomForgotUsernameForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100, required=True)
