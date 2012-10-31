from django.contrib.auth.models import User
import factory

from eca_catalogue.tests.models import ProductCategory, Product, SellingPoint


class UserFactory(factory.Factory):
    FACTORY_FOR = User

    username = factory.Sequence(lambda n: "User %s" % n)


class ProductCategoryFactory(factory.Factory):
    FACTORY_FOR = ProductCategory

    name = factory.Sequence(lambda n: "Product category %s" % n)
    slug = factory.Sequence(lambda n: "product-category-%s" % n)


class ProductFactory(factory.Factory):
    FACTORY_FOR = Product

    name = factory.Sequence(lambda n: "Product %s" % n)
    slug = factory.Sequence(lambda n: "product-%s" % n)
    item_number = factory.Sequence(lambda n: n)


class SellingPointFactory(factory.Factory):
    FACTORY_FOR = SellingPoint

    text = "Some text"

