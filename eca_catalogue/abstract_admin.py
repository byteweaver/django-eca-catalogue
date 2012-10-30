from django.contrib import admin
from django.db import models
from django.forms.widgets import TextInput

from treebeard.admin import TreeAdmin

from abstract_models import AbstractSellingPoint


class AbstractProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class AbstractNestedProductCategoryAdmin(TreeAdmin):
    prepopulated_fields = {"slug": ("name",)}

class AbstractProductAdmin(admin.ModelAdmin):
    list_display = ['item_number', 'name',]
    prepopulated_fields = {"slug": ("name",)}

class AbstractSellingPointAdmin(admin.ModelAdmin):
    """name your foreign key to product model "product" in order to fully utilize this class"""
    search_fields = ['text', 'product__name', 'product__item_number',]
    list_display = ['product', 'text',]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '150'})},
    }

class AbstractSellingPointInline(admin.StackedInline):
    """set model=YourSellingPointModel in order to get this working"""
    extra = 0
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '150'})},
    }

