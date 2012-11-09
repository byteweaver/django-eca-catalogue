from django.contrib import admin
from django.db import models
from django.forms.widgets import TextInput
from django.utils.translation import ugettext_lazy as _

from treebeard.admin import TreeAdmin

from abstract_models import AbstractSellingPoint


# fieldset for PackageMeasurementMixin, use like: fieldsets.append(package_measurement_fieldset)
package_measurement_fieldset = [_("Package measurement"), {
    'fields': ['length', 'width', 'height', 'weight']
}]

class NSDMixinAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'slug',]
    search_fields = ['name',]


class AbstractProductCategoryAdmin(NSDMixinAdmin):
    pass


class AbstractNestedProductCategoryAdmin(TreeAdmin, NSDMixinAdmin):
    pass


class AbstractProductAdmin(admin.ModelAdmin):
    list_display = ['item_number', 'name', 'slug']
    search_fields = ['name', 'item_number', ]
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = [
        [_("Basics"), {
            'fields': ['name', 'slug', 'item_number', 'description',],
        }],
    ]


class AbstractSellingPointAdmin(admin.ModelAdmin):
    """name your foreign key to product model "product" in order to fully utilize this class"""
    search_fields = ['text', 'product__name', 'product__item_number',]
    list_display = ['product', 'text',]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '150'})},
    }


class AbstractWashingInstructionAdmin(admin.ModelAdmin):
    list_display = ['text', 'render_icon',]
    search_fields = ['text',]

