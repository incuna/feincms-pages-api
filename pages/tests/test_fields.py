import mock

from django.test import TestCase

from ..fields import AbsoluteURLIdentityField


class AbsoluteURLIdentityFieldTest(TestCase):
    def test_get_url(self):
        field = AbsoluteURLIdentityField()
        obj = mock.MagicMock()
        view_name = mock.MagicMock()
        request = mock.MagicMock()
        format = mock.MagicMock()

        with mock.patch.object(obj, 'get_absolute_url') as get_absolute_url:
            field.get_url(obj, view_name, request, format)
        get_absolute_url.assert_called_once_with(request)
