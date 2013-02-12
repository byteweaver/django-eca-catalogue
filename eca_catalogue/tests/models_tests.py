from django.test import TestCase

from eca_catalogue.tests.factories import ProductFactory


class ProductTestCase(TestCase):
    def test_model(self):
        obj = ProductFactory()
        self.assertTrue(obj.pk)

