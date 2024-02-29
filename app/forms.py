from django import forms
from .models import CloudCredentials

class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(choices=(("title", "Title"), ("contributor", "Contributor")))

class CloudCredentialsForm(forms.ModelForm):
    class Meta:
        model = CloudCredentials
        fields = ['name', 'enabled']

    def __init__(self, *args, **kwargs):
        super(CloudCredentialsForm, self).__init__(*args, **kwargs)
        self.fields['aws_access_key'] = forms.CharField(required=False)
        self.fields['aws_secret_key'] = forms.CharField(required=False)
        self.fields['gcp_api_key'] = forms.CharField(required=False)
        self.fields['azure_api_key'] = forms.CharField(required=False)