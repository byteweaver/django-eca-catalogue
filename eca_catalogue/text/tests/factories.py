from django.contrib.auth.models import User
import factory

from eca_catalogue.tests.factories import ProductFactory
from eca_catalogue.text.tests.models import SellingPoint


class SellingPointFactory(factory.Factory):
    FACTORY_FOR = SellingPoint

    product = ProductFactory()

    text = "Some text"

