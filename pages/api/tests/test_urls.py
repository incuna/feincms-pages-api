from django.core.urlresolvers import resolve, reverse
from django.test import TestCase

from .. import views


class TestURLs(TestCase):
    """Ensure the pages urls work."""
    def test_page_detail_url(self):
        url = reverse('pages:page-detail', kwargs={'pk': 1})
        view_name = resolve(url).func.__name__
        self.assertEqual(view_name, views.PageViewSet.__name__)

    def test_page_list_url(self):
        url = reverse('pages:page-list')
        view_name = resolve(url).func.__name__
        self.assertEqual(view_name, views.PageViewSet.__name__)

    def test_group_url(self):
        url = reverse('pages:group-detail', kwargs={'slug': 'slug'})
        view_name = resolve(url).func.__name__
        self.assertEqual(view_name, views.GroupView.__name__)
