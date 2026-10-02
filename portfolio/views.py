from django.shortcuts import render


def base_views(request):
    return render(request, "portfolio/base.html")



def portfolio_home_views(request):
    return render(request, "portfolio/home.html")


def about_views(request):
    return render(request, "portfolio/about.html")


def cv_views(request):
    return render(request, "portfolio/cv.html")


def education_views(request):
    return render(request, "portfolio/education.html")


def experience_views(request):
    return render(request, "portfolio/experience.html")


def certifications_views(request):
    return render(request, "portfolio/certifications.html")


def services_views(request):
    return render(request, "portfolio/services.html")
