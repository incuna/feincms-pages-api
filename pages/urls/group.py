from django.conf.urls import url

from pages import views


urlpatterns = [
    url(
        r'^group/(?P<slug>[a-z0-9-]+)/?',
        views.GroupView.as_view(),
        name='group-detail',
    ),
]
