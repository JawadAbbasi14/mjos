from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    # portfolio is the landing (/) page of mjos now thats why first parameter is Empety
    path('portfolio/',include('portfolio.urls')),

]

