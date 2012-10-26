from django.contrib.auth.models import User
import factory

from eca_catalogue.tests.models import ProductCategory


class UserFactory(factory.Factory):
    FACTORY_FOR = User

    username = factory.Sequence(lambda n: "User %s" % n)

class ProductCategoryFactory(factory.Factory):
    FACTORY_FOR = ProductCategory

    name = factory.Sequence(lambda n: "Product category %s" % n)
    slug = factory.Sequence(lambda n: "product-category-%s" % n)

