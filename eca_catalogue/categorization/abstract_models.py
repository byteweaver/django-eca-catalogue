from django.db import models
from django.utils.translation import ugettext_lazy as _

from treebeard.mp_tree import MP_Node


class AbstractProductCategory(models.Model):
    name = models.CharField(_("Name"), max_length=128, unique=True)
    description = models.TextField(_("Description"), blank=True, null=True)

    class Meta:
        abstract = True
        verbose_name = _("Product category")
        verbose_name_plural = _("Product categories")
        ordering = ['name']

    def __unicode__(self):
        return self.name


class AbstractNestedProductCategory(AbstractProductCategory, MP_Node):
    class Meta:
        abstract = True

    def __unicode__(self):
        if not self.is_root():
            return unicode(self.get_parent()) + " -> " + self.name
        return self.name

