from django.contrib.auth.models import User
from django.db import models


class XuProfile(User):
    org = models.TextField(blank=True)
    org_role = models.TextField(blank=True)
