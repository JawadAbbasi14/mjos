from django.shortcuts import render
from django.db.models import Q
from .models import Project, Category
from django.shortcuts import redirect, render

def project_list_view(request):
    query = request.GET.get('name')
    projects = Project.objects.all()
    print(query)

    if query:
        Q(title__icontains=query) | Q(description__icontains=query)

    return render(request,'projects/projectform.html',{"projects":projects})