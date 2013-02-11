from django.test import TestCase

from eca_catalogue.text.tests.factories import SellingPointFactory


class SellingPointTest(TestCase):
    def test_model(self):
        obj = SellingPointFactory()
        self.assertTrue(obj.pk)

