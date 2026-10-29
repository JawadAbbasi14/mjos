from django.shortcuts import render


def platform_home(request):
    return render(request, "mjos/home.html")