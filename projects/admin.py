from django.contrib import admin
from .models import Category, Project


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'created_at')
    search_fields = ('title', 'category__name')
    list_filter = ('is_featured', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
