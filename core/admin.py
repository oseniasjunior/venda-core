from django.contrib import admin
from django.contrib.admin import TabularInline

from core import models


# Register your models here.

@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'modified_at']
    list_display_links = ['id', 'name', 'active', 'modified_at']
    search_fields = ['name']
    list_per_page = 10


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'modified_at']
    list_display_links = ['id', 'name', 'active', 'modified_at']
    search_fields = ['name']
    list_per_page = 10


class CategoryInLine(TabularInline):
    model = models.ProductCategory
    extra = 1


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'active', 'modified_at']
    list_display_links = ['id', 'name', 'price', 'active', 'modified_at']
    search_fields = ['name']
    list_per_page = 10
    inlines = [CategoryInLine]


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'salary', 'gender', 'department', 'active', 'modified_at']
    list_display_links = ['id', 'name', 'salary', 'gender', 'department', 'active', 'modified_at']
    search_fields = ['name']
    list_per_page = 10
