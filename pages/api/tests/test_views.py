from unittest.mock import patch

from rest_framework.reverse import reverse

from .. import views
from . import factories
from incuna_test_utils.testcases.api_request import APIRequestTestCase
from pages.tests.utils import TEST_SERVER
from pages.utils import build_url


def get_expected(page):
    return {
        'id': page.pk,
        'url': TEST_SERVER + page.get_absolute_url(),
        'name': page.name,
        'slug': page.slug,
        'regions': {
            'abstract': '',
            'body': 'Wow!',
        },
    }


class TestPageViewSet(APIRequestTestCase):
    view_class = views.PageViewSet

    def test_get_detail(self):
        """Test GET Page detail."""
        page = factories.PageFactory.create()
        page.richtextcontent_set.create(region='body', text='Wow!')

        request = self.create_request()
        view = self.view_class.as_view({'get': 'retrieve'})
        response = view(request, pk=page.pk)
        self.assertEqual(response.status_code, 200)

        expected = get_expected(page)
        self.assertEqual(response.data, expected)

    def test_get_list(self):
        """Test GET Page list."""
        page = factories.PageFactory.create()
        page.richtextcontent_set.create(region='body', text='Wow!')

        request = self.create_request()
        response = self.view_class.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)

        expected = [get_expected(page)]
        self.assertEqual(response.data, expected)

    def test_filtered_list(self):
        """Test filtering by PageGroup."""
        page, other_page = factories.PageFactory.create_batch(2)
        page_group = factories.PageGroupFactory.create()
        factories.PageGroupItemFactory.create(page=page, group=page_group)

        request = self.create_request()
        request.QUERY_PARAMS = {'slug': page_group.slug}
        view = self.view_class()
        view.request = request
        queryset = view.get_queryset()

        self.assertIn(page, queryset)
        self.assertNotIn(other_page, queryset)


class TestPageGroupView(APIRequestTestCase):
    view_class = views.PageGroupView

    url_path = 'pages.api.models.PageGroup.get_absolute_url'
    mocked_url = '/mocked_url'

    def get_expected(self, page_group):
        slug = page_group.slug
        return {
            'url': self.mocked_url,
            'slug': slug,
            'links': {
                'pages': build_url(reverse('pages:page-list'), {'slug': slug}),
            },
        }

    @patch(url_path)
    def test_get(self, pagegroup_url):
        pagegroup_url.return_value = self.mocked_url
        page_group = factories.PageGroupFactory.create()

        request = self.create_request()
        view = self.view_class.as_view()
        response = view(request, slug=page_group.slug)
        self.assertEqual(response.status_code, 200)

        expected = self.get_expected(page_group)
        self.assertEqual(response.data, expected)
