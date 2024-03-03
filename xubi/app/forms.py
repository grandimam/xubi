from django import forms

from xubi.app.models import CloudProvider
from xubi.login.models import XuProfile


class CloudProviderForm(forms.ModelForm):
    class Meta:
        model = CloudProvider
        fields = ['name', 'enabled']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if not username or not password:
            raise forms.ValidationError('Username already exists..')
        else:
            db = XuProfile.objects.filter(username=username)
            if not db:
                raise forms.ValidationError('Username already exists..')
        return cleaned_data
