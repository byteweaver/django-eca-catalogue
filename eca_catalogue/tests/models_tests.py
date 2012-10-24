from django.test import TestCase

from eca_catalogue.tests.models import NestedProductCategory


class NestedProductCategoryTestCase(TestCase):
    def test_model(self):
        obj = NestedProductCategory.add_root(name="cat1", slug="cat1")
        self.assertTrue(obj.pk)

