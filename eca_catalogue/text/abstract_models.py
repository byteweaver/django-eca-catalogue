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

