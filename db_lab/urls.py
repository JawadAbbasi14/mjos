# ==============================================================================
# FILE: db_lab/urls.py
# PURPOSE: Sub-application URL routing configuration map.
# DETAILS: Binds clear custom path strings to respective SQL and NoSQL controller views.
# ==============================================================================

from django.urls import path
from . import views

# Routing configurations mapped out for clean multi-database entry points
urlpatterns = [
    path('',views.read_products,name="db_home"),
    path("create", views.create_product, name="create"),
    path('delete/<int:product_id>/', views.delete_product, name="delete"),
    path('update/<int:product_id>/', views.update_product, name="update")
    

]
