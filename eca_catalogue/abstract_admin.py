from treebeard.admin import TreeAdmin


class AbstractNestedProductCategoryAdmin(TreeAdmin):
    prepopulated_fields = {"slug": ("name",)}

