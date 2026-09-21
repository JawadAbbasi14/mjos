from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Feedback

class Signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "remember", "age", "bio", "password1", "password2"]
        
        # Yeh naya hissa hai: Har field ko specific HTML attributes dena
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apna username likhein'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@mail.com'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'min': '18'}), # Minimum age 18
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                    }

# USer feed back form
class Feedback_form(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['username', 'user_feedback'] 

       
