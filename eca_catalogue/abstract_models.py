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


class AbstractMaterial(models.Model):
    name = models.CharField(_("Name"), max_length=20, unique=True)

    class Meta:
        abstract = True
        verbose_name = _("Material")
        verbose_name_plural = _("Material")
        ordering = ['name']

    def __unicode__(self):
        return self.name


class AbstractMaterialPercentage(models.Model):
    """Intermediate model"""
    material = models.ForeignKey('Material', related_name='material_percentages')
    percentage = models.PositiveIntegerField(_("Percentage"), help_text=_("Between 0 and 100"))

    class Meta:
        abstract = True
        unique_together = (("material", "percentage"),)

    def __unicode__(self):
        return "%s%% %s" % (self.percentage, self.material.name)


class AbstractMaterialComposition(models.Model):
    material_percentages = models.ManyToManyField('MaterialPercentage', verbose_name=_("Material percentages"))

    class Meta:
        abstract = True
        verbose_name = _("Material composition")
        verbose_name_plural = _("Material compositions")

    def __unicode__(self):
        percentages = []
        for mp in self.material_percentages.all():
            percentages.append("%d%% %s" % (mp.percentage, mp.material.name))
        return " ".join(percentages)


class AbstractProductMaterial(models.Model):
    """Intermediate model"""
    part = models.CharField(_("Part"), max_length=25, blank=True)
    material_composition = models.ForeignKey('MaterialComposition')
    product = models.ForeignKey('Product')

    class Meta:
        abstract = True
        verbose_name = _("Material")
        verbose_name_plural = _("Materials")

    def __unicode__(self):
        if self.part != "":
            return "%s %s" % (self.part, unicode(self.material_composition))
        else:
            return unicode(self.material_composition)

