import factory

from .. import models


class PageFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Page

    name = factory.Sequence(lambda n: 'Page {}'.format(n))
    slug = factory.Sequence(lambda n: 'page-{}'.format(n))


class GroupFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Group

    slug = factory.Sequence(lambda n: 'group-{}'.format(n))


class GroupItemFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.GroupItem

    page = factory.SubFactory(PageFactory)
    group = factory.SubFactory(GroupFactory)
    sort_order = factory.Sequence(lambda n: n)
