from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractProduct(models.Model):
    item_number = models.CharField(_("Item number"), max_length=255, unique=True)
    name = models.CharField(_("Name"), max_length=128)
    description = models.TextField(_("Description"), blank=True, null=True)

    class Meta:
        abstract = True
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ['item_number']

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.item_number)

