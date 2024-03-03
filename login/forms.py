from django import forms

from login.models import XuProfile


class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = XuProfile
        fields = ['username', 'password']
