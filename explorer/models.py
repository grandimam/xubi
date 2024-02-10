from django.db import models

class CloudProvider(models.Model):
    name = models.CharField(max_length=50)

class CloudCredentials(models.Model):
    provider = models.ForeignKey(CloudProvider, on_delete=models.CASCADE)
    access_key = models.CharField(max_length=100)
    secret_key = models.CharField(max_length=100)
    # Add other necessary fields

class CloudCostData(models.Model):
    provider = models.ForeignKey(CloudProvider, on_delete=models.CASCADE)
    # Add other necessary fields