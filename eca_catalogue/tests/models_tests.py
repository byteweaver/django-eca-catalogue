from django.test import TestCase

from eca_catalogue.tests.models import NestedProductCategory
from eca_catalogue.tests.factories import ProductCategoryFactory, ProductFactory, SellingPointFactory


class ProductCategoryTestCase(TestCase):
    def test_model(self):
        obj = ProductCategoryFactory()
        self.assertTrue(obj.pk)


class NestedProductCategoryTestCase(TestCase):
    def test_model(self):
        obj = NestedProductCategory.add_root(name="cat1", slug="cat1")
        self.assertTrue(obj.pk)


class ProductTestCase(TestCase):
    def test_model(self):
        obj = ProductFactory()
        self.assertTrue(obj.pk)


class SellingPointTest(TestCase):
    def test_model(self):
        obj = SellingPointFactory()
        self.assertTrue(obj.pk)

