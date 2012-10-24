from treebeard.admin import TreeAdmin


class AbstractProductCategoryAdmin(TreeAdmin):
    prepopulated_fields = {"slug": ("name",)}

