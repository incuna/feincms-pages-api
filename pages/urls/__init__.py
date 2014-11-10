from django.conf.urls import include, url


urlpatterns = [
    url(r'', include('pages.urls.page')),
    url(r'', include('pages.urls.group')),
]
