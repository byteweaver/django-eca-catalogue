from django.contrib import admin
from django.db import models


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

