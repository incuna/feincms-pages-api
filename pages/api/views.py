from rest_framework import generics, viewsets

from . import models, serializers


class PageViewSet(viewsets.ReadOnlyModelViewSet):
    model = models.Page
    serializer_class = serializers.PageSerializer

    def get_queryset(self):
        queryset = super(PageViewSet, self).get_queryset()
        slug = self.request.QUERY_PARAMS.get('slug')

        if slug is None:
            return queryset

        return queryset.filter(groupitem__group__slug=slug)


class GroupView(generics.RetrieveAPIView):
    model = models.Group
    serializer_class = serializers.GroupSerializer
