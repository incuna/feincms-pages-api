from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import models, serializers


class PageViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'slug'
    queryset = models.Page.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        """Get the appropriate serializer using the regions_format."""
        regions_format = self.request.query_params.get('regions_format')
        if regions_format == 'json':
            return serializers.JsonPageSerializer
        return serializers.PageSerializer

    def get_queryset(self):
        queryset = super(PageViewSet, self).get_queryset()
        group_slug = self.request.query_params.get('group')

        if group_slug is None:
            return queryset

        return queryset.filter(groupitem__group__slug=group_slug)


class GroupView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer
