from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    name = models.CharField(max_feild=200, null=True)
    email = models.CharField(max_feild=200, null=True)