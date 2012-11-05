from django.db import models
from django.utils.translation import ugettext_lazy as _

from treebeard.mp_tree import MP_Node


class NSDMixin(models.Model):
    name = models.CharField(_("Name"), max_length=128)
    slug = models.SlugField(_("Slug"), max_length=128, unique=True)
    description = models.TextField(_("Description"), blank=True, null=True)

    class Meta:
        abstract = True


class AbstractProductCategory(NSDMixin):
    class Meta:
        abstract = True
        verbose_name = _("Product category")
        verbose_name_plural = _("Product categories")
        ordering = ['name']

    def __unicode__(self):
        return self.name


class AbstractNestedProductCategory(MP_Node, NSDMixin):
    class Meta:
        abstract = True
        verbose_name = _("Nested product category")
        verbose_name_plural = _("Nested product categories")
        ordering = ['name']

    def __unicode__(self):
        if not self.is_root():
            return unicode(self.get_parent()) + " -> " + self.name
        return self.name


class AbstractProduct(NSDMixin):
    item_number = models.CharField(_("Item number"), max_length=255, unique=True)

    class Meta:
        abstract = True
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ['name']

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.item_number)


class AbstractSellingPoint(models.Model):
    text = models.CharField(_("Text"), max_length=255)

    class Meta:
        abstract = True
        verbose_name = _("Selling point")
        verbose_name_plural = _("Selling points")

    def __unicode__(self):
        return self.text


class PackageMeasurementMixin(models.Model):
    length = models.DecimalField(_("Length"), max_digits=5, decimal_places=1)
    width = models.DecimalField(_("Width"), max_digits=5, decimal_places=1)
    height = models.DecimalField(_("Height"), max_digits=5, decimal_places=1)
    weight = models.DecimalField(_("Weigth"), max_digits=5, decimal_places=1)

    class Meta:
        abstract = True


class AbstractMaterial(models.Model):
    name = models.CharField(_("Name"), max_length=20, unique=True)

    class Meta:
        abstract = True
        verbose_name = _("Material")
        verbose_name_plural = _("Material")

    def __unicode__(self):
        return self.name



