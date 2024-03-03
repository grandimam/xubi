from django.db import models


class CloudProvider(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    enabled = models.CharField(max_length=100, blank=False)
    aws_access_key = models.CharField(max_length=100, blank=True)
    aws_secret_key = models.CharField(max_length=100, blank=True)
    gcp_api_key = models.CharField(max_length=100, blank=True)
    azure_api_key = models.CharField(max_length=100, blank=True)
