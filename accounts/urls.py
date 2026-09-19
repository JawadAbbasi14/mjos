from django.urls import path
from . import views

urlpatterns = [
   
    path('signup/',views.signup_views,name="signup"),
    path('login/',views.login_views,name="login"),
    path('dashboard/',views.dashboard,name="dashboard")


]
