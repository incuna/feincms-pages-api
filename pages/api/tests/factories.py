from .. import models
import factory


class PageFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Page

    name = factory.Sequence(lambda n: 'Page {}'.format(n))
    slug = factory.Sequence(lambda n: 'page-{}'.format(n))


class PageGroupFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.PageGroup

    slug = factory.Sequence(lambda n: 'page-group-{}'.format(n))


class PageGroupItemFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.PageGroupItem

    page = factory.SubFactory(PageFactory)
    group = factory.SubFactory(PageGroupFactory)
    sort_order = factory.Sequence(lambda n: n)
