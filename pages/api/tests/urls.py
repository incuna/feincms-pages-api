from django.conf.urls import include, patterns, url


urlpatterns = patterns('',
    url(r'', include(
        patterns('',
            url(r'', include('pages.api.urls.page')),
            url(r'', include('pages.api.urls.page_group')),
        ),
        namespace='pages',
    ))
)
