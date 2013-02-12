from django.utils.translation import ugettext_lazy as _


# fieldset for PackageMeasurementMixin, use like: fieldsets.append(package_measurement_fieldset)
package_measurement_fieldset = [_("Package measurement"), {
    'fields': ['length', 'width', 'height', 'weight']
}]

