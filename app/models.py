from django.db import models

class CloudCredentials(models.Model):
    name = models.CharField(max_length=50)
    access_key = models.CharField(max_length=100)
    secret_key = models.CharField(max_length=100)
    enabled = models.CharField(max_length=100)

class CloudCostData(models.Model):
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    service = models.CharField(max_length=255)
    usage_type = models.CharField(max_length=255)
    usage_value = models.FloatField()
    currency = models.CharField(max_length=10)