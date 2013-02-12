from django.contrib import admin


class AbstractMaterialAdmin(admin.ModelAdmin):
    search_fields = ['name',]


class AbstractMaterialPercentageAdmin(admin.ModelAdmin):
    list_display = ['material', 'percentage',]
    search_fields = ['material__name', 'percentage',]
    list_filter = ['material',]


class AbstractMaterialCompositionAdmin(admin.ModelAdmin):
    filter_horizontal = ['material_percentages',]
    list_filter = ['material_percentages__material',]


class AbstractProductMaterialAdmin(admin.ModelAdmin):
    list_display = ['material_composition', 'product',]
    raw_id_fields = ['product',]

