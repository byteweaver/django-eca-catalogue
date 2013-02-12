from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class AbstractProductAdmin(admin.ModelAdmin):
    list_display = ['item_number', 'name',]
    search_fields = ['item_number', 'name',]
    fieldsets = [
        [_("Basics"), {
            'fields': ['item_number', 'name', 'description',],
        }],
    ]

