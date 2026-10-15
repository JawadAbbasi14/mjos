from django.urls import path
from . import views
urlpatterns = [
    path('',views.database_start,name="db_start")
]
