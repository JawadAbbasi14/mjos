from django.urls import reverse


"""Curated public applications; add a real landing URL name for each module."""

MODULES = (
    {
        "id": "portfolio",
        "name": "Portfolio",
        "description": "Professional profile, work, learning, and credentials.",
        "url_name": "portfolio_home",
        "active_url_names": (
            "portfolio_home",
            "portfolio_base",
            "about",
            "cv",
            "education",
            "experience",
            "certifications",
            "services",
        ),
    },
    {
        "id": "projects",
        "name": "Projects",
        "description": "Browse projects by title, description, and category.",
        "url_name": "project_form",
        "active_url_names": ("project_form", "project_detail"),
    },
    {
        "id": "database-lab",
        "name": "Database Lab",
        "description": "Create and manage product records in the database lab.",
        "url_name": "db_home",
        "active_url_names": ("db_home", "create", "update"),
    },
)


def application_modules(request):
    current_name = getattr(getattr(request, "resolver_match", None), "url_name", None)
    modules = [
        {
            **module,
            "url": reverse(module["url_name"]),
            "is_active": current_name in module["active_url_names"],
        }
        for module in MODULES
    ]
    return {"application_modules": modules}
