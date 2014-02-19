from django.conf.urls import patterns, url

from .. import views


urlpatterns = patterns('',
    url(
        r'group/(?P<slug>[a-z0-9-]+)/?',
        views.GroupView.as_view(),
        name='group-detail',
    ),
)
