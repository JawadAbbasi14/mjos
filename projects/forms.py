from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'category', 'description', 'github_url', 'live_demo_url', 'is_featured']

  
        