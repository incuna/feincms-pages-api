from rest_framework import generics, viewsets

from . import models, serializers


class PageViewSet(viewsets.ReadOnlyModelViewSet):
    model = models.Page
    serializer_class = serializers.PageSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.request.QUERY_PARAMS.get('slug')

        if slug is None:
            return queryset

        return queryset.filter(pagegroupitem__group__slug=slug)


class PageGroupView(generics.RetrieveAPIView):
    model = models.PageGroup
    serializer_class = serializers.PageGroupSerializer
