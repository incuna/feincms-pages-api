from mock import patch, MagicMock

from django.test import TestCase

from .. import models
from . import factories


class TestPageModel(TestCase):
    def test_fields(self):
        expected = {
            'id',
            'name',
            'slug',
            'groupitem',
            'richtextcontent_set',
        }

        fields = models.Page._meta.get_all_field_names()

        # assertItemsEqual has been renamed assertCountEqual in python version 3
        try:
            # python 3
            self.assertCountEqual(fields, expected)
        except AttributeError:
            # python 2.7
            self.assertItemsEqual(fields, expected)

    def test_slug_unique(self):
        slug_field = models.Page._meta.get_field_by_name('slug')[0]
        self.assertTrue(slug_field.unique)

    def test_str(self):
        page = factories.PageFactory.build()
        self.assertEqual(str(page), page.name)


class TestGroupModel(TestCase):
    def test_fields(self):
        expected = {
            'id',
            'slug',
            'groupitem',
        }

        fields = models.Group._meta.get_all_field_names()

        # assertItemsEqual has been renamed assertCountEqual in python version 3
        try:
            # python 3
            self.assertCountEqual(fields, expected)
        except AttributeError:
            # python 2.7
            self.assertItemsEqual(fields, expected)

    def test_str(self):
        group = factories.GroupFactory.build()
        self.assertEqual(str(group), group.slug)

    def test_get_absolute_url(self):
        group = factories.GroupFactory.create()
        request = MagicMock()

        with patch('pages.models.reverse') as patched_reverse:
            group.get_absolute_url(request)

        patched_reverse.assert_called_once_with(
            'pages:group-detail',
            kwargs={'slug': group.slug},
            request=request,
        )


class TestGroupItem(TestCase):
    def test_fields(self):
        expected = {
            'id',
            'page',
            'group',
            'sort_order',
        }

        fields = models.GroupItem._meta.get_all_field_names()

        # assertItemsEqual has been renamed assertCountEqual in python version 3
        try:
            # python 3
            self.assertCountEqual(fields, expected)
        except AttributeError:
            # python 2.7
            self.assertItemsEqual(fields, expected)
