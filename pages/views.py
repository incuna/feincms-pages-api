from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import models, serializers


class PageViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'slug'
    model = models.Page
    serializer_class = serializers.PageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super(PageViewSet, self).get_queryset()
        group_slug = self.request.QUERY_PARAMS.get('group')

        if group_slug is None:
            return queryset

        return queryset.filter(groupitem__group__slug=group_slug)


class GroupView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    model = models.Group
    serializer_class = serializers.GroupSerializer
