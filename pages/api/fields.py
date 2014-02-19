from rest_framework import serializers


class AbsoluteURLMixin(object):
    """Use get_absolute_url to get the field's api endpoint."""

    def __init__(self, *args, **kwargs):
        # HyperlinkedFields expect a view_name to be passed, so pass None.
        kwargs.setdefault('view_name')
        super(AbsoluteURLMixin, self).__init__(*args, **kwargs)

    def get_url(self, obj, view_name, request, format):
        return obj.get_absolute_url(request)


class AbsoluteURLIdentityField(AbsoluteURLMixin, serializers.HyperlinkedIdentityField):
    pass
