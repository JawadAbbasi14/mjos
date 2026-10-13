from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Category, Project

def project_list_view(request):
    query = request.GET.get("q", "").strip()
    project_category = request.GET.get("project_category", "").strip()
    projects = Project.objects.select_related("category").all()

    if query:
        projects = projects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    if project_category:
        projects = projects.filter(category__slug=project_category)

    paginator = Paginator(projects, 5)
    page_obj = paginator.get_page(request.GET.get("page"))

    pagination_params = request.GET.copy()
    pagination_params.pop("page", None)

    return render(
        request,
        "projects/projectform.html",
        {
            "projects": page_obj,
            "categories": Category.objects.all(),
            "query": query,
            "selected_category": project_category,
            "pagination_query": pagination_params.urlencode(),
        },
    )


def project_detail(request, slug):
    project = get_object_or_404(
        Project.objects.select_related("category"),
        slug=slug,
    )
    return render(
        request,
        "projects/projects_detail.html",
        {"project": project},
    )

