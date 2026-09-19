from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class Customeuser(UserAdmin):
    # Admin list view mein dikhane ke liye
    list_display = ('username', 'age', 'bio','remember')
    
    # Sahi spelling 'fieldsets' hai aur yeh class ke andar hona chahiye
    fieldsets = UserAdmin.fieldsets + (
        ('Karobar / Additional Info', {'fields': ('bio', 'age','remember')}),
    )
    
    # Naya user create karte waqt agar fields chahiye hon
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Karobar / Additional Info', {'fields': ('bio', 'age', 'remember')}),
    )

# Model aur custom admin class ko register karein
admin.site.register(User, Customeuser)
