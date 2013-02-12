from django.db import models
from django.utils.translation import ugettext_lazy as _


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
        ordering = ['-percentage']

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
        return ", ".join(percentages)


class AbstractProductMaterial(models.Model):
    """Links a material composition to a product, may also be used as an intermediate model."""
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

