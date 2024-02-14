from django import forms
from .models import CloudCredentials

class CloudCredentialsForm(forms.ModelForm):
    class Meta:
        model = CloudCredentials
        fields = ['name', 'enabled']

    def __init__(self, *args, **kwargs):
        super(CloudCredentialsForm, self).__init__(*args, **kwargs)
        self.fields['aws_access_key'] = forms.CharField(required=False)
        self.fields['aws_secret_key'] = forms.CharField(required=False)
        self.fields['aws_access_key'].label = 'AWS Access Key'
        self.fields['aws_secret_key'].label = 'AWS Secret Key'

        self.fields['gcp_api_key'] = forms.CharField(required=False)
        self.fields['azure_api_key'] = forms.CharField(required=False)
        self.fields['gcp_api_key'].label = 'GCP API Key'
        self.fields['azure_api_key'].label = 'Azure API Key'