from django.contrib import admin

from treebeard.admin import TreeAdmin


class AbstractProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class AbstractNestedProductCategoryAdmin(TreeAdmin):
    prepopulated_fields = {"slug": ("name",)}

class AbstractProductAdmin(admin.ModelAdmin):
    list_display = ['item_number', 'name',]
    prepopulated_fields = {"slug": ("name",)}

