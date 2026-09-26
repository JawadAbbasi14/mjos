from django.urls import path
from . import views


urlpatterns = [
    path("",views.portfolio_views,name='home')
]
