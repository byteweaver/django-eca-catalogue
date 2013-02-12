from django.db import models
from django.utils.translation import ugettext_lazy as _


class PackageMeasurementMixin(models.Model):
    length = models.FloatField(_("Length"), default=0)
    width = models.FloatField(_("Width"), default=0)
    height = models.FloatField(_("Height"), default=0)
    weight = models.FloatField(_("Weigth"), default=0)

    class Meta:
        abstract = True

