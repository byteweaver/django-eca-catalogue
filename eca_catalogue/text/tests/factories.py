from django.contrib.auth.models import User
import factory

from eca_catalogue.tests.factories import ProductFactory
from eca_catalogue.text.tests.models import SellingPoint, WashingInstruction


class SellingPointFactory(factory.Factory):
    FACTORY_FOR = SellingPoint

    product = ProductFactory()

    text = "Some text"


class WashingInstructionFactory(factory.Factory):
    FACTORY_FOR = WashingInstruction

    icon = "icon.png"
    text = "text"

