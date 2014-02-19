from django.conf.urls import include, patterns, url


urlpatterns = patterns('',
    url(r'', include('pages.urls.page')),
    url(r'', include('pages.urls.group')),
)
