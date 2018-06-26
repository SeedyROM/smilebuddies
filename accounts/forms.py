from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms.models import ModelForm

from accounts.models import Account


class AccountCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ('username', 'email')

class AccountChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = UserCreationForm.Meta.fields + ('location',)
