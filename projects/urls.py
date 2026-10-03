from django.urls import path
from . import views

urlpatterns = [
    path('',views.project_list_view, name='project_form')
]
