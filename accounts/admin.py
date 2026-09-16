from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from .models import User
# Register your models here.

class Customeuser(UserAdmin):
    list_display = ('username','age','bio')


filedset = UserAdmin.fieldsets + (
        ('Karobar / Additional Info', {'fields': ('bio', 'age')}),
    )
admin.site.register(User,Customeuser)