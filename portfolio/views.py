from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def base_views(request):
    return render("request",'portfolio/home.html')



@login_required(login_url="login")
def portfolio_home_views(request):
    return render(request, "portfolio/home.html")


def about_views(request):
    return render(request, "portfolio/about.html")


def cv_views(request):
    return HttpResponse('portfolio cv html')


def education_views(request):
    return HttpResponse('portfolio education html')


def experience_views(request):
    return HttpResponse('portfolio experience html')


def certifications_views(request):
    return HttpResponse('portfolio certifications html')


def services_views(request):
    return HttpResponse('portfolio services html')
