from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Feedback

class Signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "remember", "age", "bio", "password1", "password2"]
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Fullname'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@mail.com'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'min': '18'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

# User feedback form (FIXED)
class Feedback_form(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['username', 'user_feedback'] 

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Fullname'}),
            'user_feedback': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your feedback here...', 'rows': 3}), # 'bio' ko badal kar 'user_feedback' kar diya
        }
