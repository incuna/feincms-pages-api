from .. import models
import factory


class PageFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Page

    name = factory.Sequence(lambda n: 'Page {}'.format(n))
    slug = factory.Sequence(lambda n: 'page-{}'.format(n))


class GroupFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Group

    slug = factory.Sequence(lambda n: 'group-{}'.format(n))


class GroupItemFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.GroupItem

    page = factory.SubFactory(PageFactory)
    group = factory.SubFactory(GroupFactory)
    sort_order = factory.Sequence(lambda n: n)
