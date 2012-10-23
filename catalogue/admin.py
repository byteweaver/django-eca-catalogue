from django.contrib import admin
from treebeard.admin import TreeAdmin

from catalogue.models import ProductCategory


class ProductCategoryAdmin(TreeAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(ProductCategory, ProductCategoryAdmin)

