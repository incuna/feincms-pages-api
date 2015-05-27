from rest_framework.reverse import reverse
from user_management.models.tests.utils import APIRequestTestCase

from pages import serializers
from pages.tests import factories
from pages.utils import build_url


class PageSerializerTest(APIRequestTestCase):
    def setUp(self):
        self.request = self.create_request()
        self.context = {'request': self.request}

    def expected_data(self, page):
        expected = {
            'id': page.pk,
            'url': page.get_absolute_url(self.request),
            'name': page.name,
            'slug': page.slug,
            'regions': page.rendered_regions(self.request),
        }
        return expected

    def test_serialize(self):
        page = factories.PageFactory.create()
        serializer = serializers.PageSerializer(page, context=self.context)
        self.assertEqual(serializer.data, self.expected_data(page))

    def test_serialize_to_json(self):
        page = factories.PageFactory.create()
        serializer = serializers.JsonPageSerializer(page, context=self.context)

        expected_data = self.expected_data(page)
        expected_data['regions'] = {'abstract': [], 'body': []}
        self.assertEqual(serializer.data, expected_data)


class GroupTest(APIRequestTestCase):
    def setUp(self):
        self.request = self.create_request()
        self.context = {'request': self.request}

    def expected_data(self, group):
        slug = group.slug
        return {
            'url': group.get_absolute_url(self.request),
            'slug': slug,
            'links': {
                'pages': build_url(
                    reverse('pages:page-list', request=self.request),
                    {'group': slug},
                ),
            },
        }

    def test_serialize(self):
        group = factories.GroupFactory.create()

        serializer = serializers.GroupSerializer(group, context=self.context)
        self.assertEqual(serializer.data, self.expected_data(group))
