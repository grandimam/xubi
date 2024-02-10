from django import forms
from .models import CloudCredentials

class CloudCredentialsForm(forms.ModelForm):
    class Meta:
        model = CloudCredentials
        fields = ['name', 'access_key', 'secret_key']