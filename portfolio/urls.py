from django.urls import path
from . import views


urlpatterns = [
    path("", views.portfolio_home_views, name='home'),
    path("base/", views.base_views, name="base"),
    path("certification/", views.certifications_views, name="certifications"),
    path("cv/", views.cv_views, name="cv"),
    path("about/", views.about_views, name="about"),
    path("education/", views.education_views, name="education"),
    path("experience/", views.experience_views, name="experience"),
    path("services/", views.services_views, name="services"),
]
