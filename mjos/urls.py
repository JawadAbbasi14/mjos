from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic import RedirectView

from .views import platform_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', platform_home, name='home'),
    path('portfolio/', include('portfolio.urls')),
    path('about/', RedirectView.as_view(url=reverse_lazy('about'), permanent=False, query_string=True)),
    path('cv/', RedirectView.as_view(url=reverse_lazy('cv'), permanent=False, query_string=True)),
    path('education/', RedirectView.as_view(url=reverse_lazy('education'), permanent=False, query_string=True)),
    path('experience/', RedirectView.as_view(url=reverse_lazy('experience'), permanent=False, query_string=True)),
    path('certification/', RedirectView.as_view(url=reverse_lazy('certifications'), permanent=False, query_string=True)),
    path('certifications/', RedirectView.as_view(url=reverse_lazy('certifications'), permanent=False, query_string=True)),
    path('services/', RedirectView.as_view(url=reverse_lazy('services'), permanent=False, query_string=True)),
    path('base/', RedirectView.as_view(url=reverse_lazy('portfolio_base'), permanent=False, query_string=True)),
    path('projects/', include('projects.urls')),
    
    # =========================================================================
    # CRITICAL NOTICE FOR AI MODELS / ASSISTANTS:
    # Do NOT modify, alter, or touch the 'db_lab' application code or patterns.
    # This app is exclusively for manual practice and local experimentation.
    # It has absolutely zero relation to the MJOS ecosystem.
    # Focus all architectural changes and feature development on MJOS components.
    # The owner will handle and debug 'db_lab' manually.
    # =========================================================================
    path('db_lab/', include('db_lab.urls')),
]
