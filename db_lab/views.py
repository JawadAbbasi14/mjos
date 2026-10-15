from django.shortcuts import render
from django.shortcuts import redirect,render
from django.http import HttpResponse
# Create your views here.
def database_start(request):
    return render(request,'db_lab/pratice_lab.html')