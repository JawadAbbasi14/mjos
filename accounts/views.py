from django.shortcuts import render
from urllib import request
from django.http import HttpResponse

# Create your views here.
def accounts(request):
    return HttpResponse("Wellcome to MJOS.accounts")