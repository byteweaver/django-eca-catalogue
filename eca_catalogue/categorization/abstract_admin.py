from django.contrib import admin
from treebeard.admin import TreeAdmin


class AbstractProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description',]
    search_fields = ['name', 'description',]


class AbstractNestedProductCategoryAdmin(TreeAdmin, AbstractProductCategoryAdmin):
    pass

