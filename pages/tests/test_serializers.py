from mock import patch

from django.test import TestCase
from rest_framework.reverse import reverse

from .. import serializers
from . import factories
from pages.utils import build_url


class PageSerializerTest(TestCase):
    def expected_data(self, page):
        expected = {
            'id': page.pk,
            'url': page.get_absolute_url(),
            'name': page.name,
            'slug': page.slug,
            'regions': page.rendered_regions(),
        }
        return expected

    def test_serialize(self):
        page = factories.PageFactory.create()
        serializer = serializers.PageSerializer(page)
        self.assertEqual(serializer.data, self.expected_data(page))


class GroupTest(TestCase):
    url_path = 'pages.models.Group.get_absolute_url'
    mocked_url = '/mocked_url'

    def expected_data(self, group):
        slug = group.slug
        return {
            'url': self.mocked_url,
            'slug': slug,
            'links': {
                'pages': build_url(reverse('pages:page-list'), {'slug': slug}),
            },
        }

    @patch(url_path)
    def test_serialize(self, group_url):
        group_url.return_value = self.mocked_url
        group = factories.GroupFactory.create()

        serializer = serializers.GroupSerializer(group)
        self.assertEqual(serializer.data, self.expected_data(group))
