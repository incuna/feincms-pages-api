from collections import OrderedDict
from unittest import TestCase

from .. import build_url


class TestUtils(TestCase):
    def test_build_url(self):
        url = 'example.com/test/'
        expected = 'example.com/test/?foo=bar&spam=eggs'

        get_params = OrderedDict((('foo', 'bar'), ('spam', 'eggs')))
        self.assertEqual(expected, build_url(url, get=get_params))
