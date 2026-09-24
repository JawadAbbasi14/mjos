from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('signup/', views.signup_views, name="signup"),
    path('login/', views.login_views, name="login"),
    path('logout/', views.logout_views, name="logout_name"),
    path('feedback/', views.feedback_views, name="feedback"),
]