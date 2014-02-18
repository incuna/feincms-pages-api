from django.conf.urls import include, patterns, url

from .. import views


urlpatterns = patterns('',
    url(
        r'pagegroup/(?P<slug>[a-z0-9-]+)/?',
        views.PageGroupView.as_view(),
        name='pagegroup-detail',
    ),
)
