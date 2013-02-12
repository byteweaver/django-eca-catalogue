from django.contrib.auth.models import User
import factory

from eca_catalogue.tests.models import Product


class UserFactory(factory.Factory):
    FACTORY_FOR = User

    username = factory.Sequence(lambda n: "User %s" % n)


class ProductFactory(factory.Factory):
    FACTORY_FOR = Product

    name = factory.Sequence(lambda n: "Product %s" % n)
    slug = factory.Sequence(lambda n: "product-%s" % n)
    item_number = factory.Sequence(lambda n: n)

