from django.contrib import admin

from treebeard.admin import TreeAdmin


class AbstractProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class AbstractNestedProductCategoryAdmin(TreeAdmin):
    prepopulated_fields = {"slug": ("name",)}

