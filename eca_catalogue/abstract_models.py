from django.db import models
from django.utils.translation import ugettext_lazy as _



class UNSDMixin(models.Model):
    name = models.CharField(_("Name"), max_length=128, unique=True)
    slug = models.SlugField(_("Slug"), max_length=128, unique=True)
    description = models.TextField(_("Description"), blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.name = self.name.strip()
        return super(UNSDMixin, self).save(*args, **kwargs)


class NSDMixin(models.Model):
    name = models.CharField(_("Name"), max_length=128)
    slug = models.SlugField(_("Slug"), max_length=128, unique=True)
    description = models.TextField(_("Description"), blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.name = self.name.strip()
        return super(NSDMixin, self).save(*args, **kwargs)


class AbstractProduct(UNSDMixin):
    item_number = models.CharField(_("Item number"), max_length=255, unique=True)

    class Meta:
        abstract = True
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ['name']

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.item_number)


class PackageMeasurementMixin(models.Model):
    length = models.FloatField(_("Length"), default=0)
    width = models.FloatField(_("Width"), default=0)
    height = models.FloatField(_("Height"), default=0)
    weight = models.FloatField(_("Weigth"), default=0)

    class Meta:
        abstract = True

