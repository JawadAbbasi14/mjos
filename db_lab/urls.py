# ==============================================================================
# FILE: db_lab/urls.py
# PURPOSE: Sub-application URL routing configuration map.
# DETAILS: Binds clear custom path strings to respective SQL and NoSQL controller views.
# ==============================================================================

from django.urls import path
from . import views

# Routing configurations mapped out for clean multi-database entry points
urlpatterns = [
    path('',views.database_start,name="start_db")
]
