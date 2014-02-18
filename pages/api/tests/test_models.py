from unittest.mock import patch, MagicMock

from django.test import TestCase

from .. import models
from . import factories


class TestPageModel(TestCase):
    def test_fields(self):
        fields = models.Page._meta.get_all_field_names()
        self.assertCountEqual(
            ('id', 'name', 'slug', 'pagegroupitem', 'richtextcontent_set'),
            fields,
        )

    def test_slug_unique(self):
        slug_field = models.Page._meta.get_field_by_name('slug')[0]
        self.assertTrue(slug_field.unique)

    def test_str(self):
        page = factories.PageFactory.build()
        self.assertEqual(str(page), page.name)


class TestPageGroupModel(TestCase):
    def test_fields(self):
        fields = models.PageGroup._meta.get_all_field_names()
        self.assertCountEqual(('id', 'slug', 'pagegroupitem'), fields)

    def test_str(self):
        page_group = factories.PageGroupFactory.build()
        self.assertEqual(str(page_group), page_group.slug)

    def test_get_absolute_url(self):
        page_group = factories.PageGroupFactory.create()
        request = MagicMock()

        with patch('pages.api.models.reverse') as patched_reverse:
            page_group.get_absolute_url(request)

        patched_reverse.assert_called_once_with(
            'pages:pagegroup-detail',
            kwargs={'slug': page_group.slug},
            request=request,
        )


class TestPageGroupItem(TestCase):
    def test_fields(self):
        fields = models.PageGroupItem._meta.get_all_field_names()
        self.assertCountEqual(('id', 'page', 'group', 'sort_order'), fields)
