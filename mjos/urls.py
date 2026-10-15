from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('portfolio.urls')),
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
