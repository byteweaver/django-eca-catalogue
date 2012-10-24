from django.test import TestCase

from eca_catalogue.tests.models import ProductCategory


class ProductCategoryTestCase(TestCase):
    def test_model(self):
        obj = ProductCategory.add_root(name="cat1", slug="cat1")
        self.assertTrue(obj.pk)

