from django.contrib.auth.models import AbstractUser
from django.db import  models

class User(AbstractUser):
   age = models.IntegerField(blank=False),
   bio = models.CharField(max_length=100,null=True)