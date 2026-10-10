from django.shortcuts import render
from django.db.models import Q
from .models import Project, Category
from django.shortcuts import redirect, render

def project_list_view(request):
    projects = Project.objects.all()
    query = request.GET.get('name')
    project_category = request.GET.get('project_category')
  
    if query:
       projects = projects.filter(
           Q(title__icontains=query) | Q(description__icontains=query)
       )
       
    if project_category:
       # Yahan 'projects =' lagaya ha takay filter save ho sake
       projects = projects.filter(
           Q(category__slug=project_category)
       )
       
    print(query, project_category)
    return render(request, "projects/projectform.html", {"projects": projects})
