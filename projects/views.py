from django.shortcuts import render
from django.db.models import Q
from .models import Project, Category

def project_list_view(request):

    # Base Queryset
    projects = Project.objects.select_related('category').all()
    categories = Category.objects.all()

    # Search Logic (Q objects)
    query = request.GET.get('q')
    print(f"{request.GET} idr laaga hua ha GET!")
    category_slug = request.GET.get('category')

    if query:
        projects = projects.filter(
            Q(title__icontains=query) | Q(github_url__icontains=query)
        )

    if category_slug:
        projects = projects.filter(category__slug=category_slug)

    context = {
        'projects': projects,
        'categories': categories,
        'selected_category': category_slug,
        'search_query': query or '',
    }
    return render(request, 'projects/projectform.html', context)