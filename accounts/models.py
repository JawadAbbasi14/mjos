from django.contrib.auth.models import AbstractUser
from django.db import  models

class User(AbstractUser):
   age = models.IntegerField(blank=False,null=True)
   bio = models.CharField(max_length=100,null=True)
   remember = models.BooleanField(default=False)



class Feedback(models.Model):
      username = models.CharField(max_length=100,null=False)
      user_feedback = models.TextField(max_length=5000,null=False)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
   
   