from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractSellingPoint(models.Model):
    text = models.CharField(_("Text"), max_length=255)
    product = models.ForeignKey('Product', related_name='selling_points')

    class Meta:
        abstract = True
        verbose_name = _("Selling point")
        verbose_name_plural = _("Selling points")

    def __unicode__(self):
        return self.text

