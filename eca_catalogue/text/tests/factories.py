from django.contrib.auth.models import User
import factory

from eca_catalogue.text.tests.models import WashingInstruction


class WashingInstructionFactory(factory.Factory):
    FACTORY_FOR = WashingInstruction

    icon = "icon.png"
    text = "text"

