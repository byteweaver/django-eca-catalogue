from django.db import models
from django.utils.translation import ugettext_lazy as _

from treebeard.mp_tree import MP_Node


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


class AbstractProductCategory(UNSDMixin):
    class Meta:
        abstract = True
        verbose_name = _("Product category")
        verbose_name_plural = _("Product categories")
        ordering = ['name']

    def __unicode__(self):
        return self.name


class AbstractNestedProductCategory(MP_Node, UNSDMixin):
    class Meta:
        abstract = True
        verbose_name = _("Nested product category")
        verbose_name_plural = _("Nested product categories")
        ordering = ['name']

    def __unicode__(self):
        if not self.is_root():
            return unicode(self.get_parent()) + " -> " + self.name
        return self.name


class AbstractProduct(UNSDMixin):
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
    product = models.ForeignKey('Product', related_name='selling_points')

    class Meta:
        abstract = True
        verbose_name = _("Selling point")
        verbose_name_plural = _("Selling points")

    def __unicode__(self):
        return self.text


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


class AbstractWashingInstruction(models.Model):
    icon = models.ImageField(verbose_name=_("Icon"), upload_to='laundry_symbols/', blank=True)
    text = models.CharField(_("Text"), max_length=255)

    class Meta:
        abstract = True
        verbose_name = _("Washing instruction")
        verbose_name_plural = _("Washing instructions")

    def __unicode__(self):
        return self.text

    def render_icon(self):
        if self.icon:
            return '<img src="%s" alt="%s" title="%s">' % (self.icon.url, self.text, self.text)
        else:
            return None
    render_icon.allow_tags = True
    render_icon.short_description = _("Icon")

