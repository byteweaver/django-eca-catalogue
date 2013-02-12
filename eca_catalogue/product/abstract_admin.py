from django.contrib import admin
from django.db import models
from django.forms.widgets import TextInput
from django.utils.translation import ugettext_lazy as _

from abstract_models import AbstractSellingPoint


class NSDMixinAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'slug',]
    search_fields = ['name',]


class AbstractProductAdmin(admin.ModelAdmin):
    list_display = ['item_number', 'name', 'slug']
    search_fields = ['name', 'item_number', ]
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = [
        [_("Basics"), {
            'fields': ['name', 'slug', 'item_number', 'description',],
        }],
    ]

