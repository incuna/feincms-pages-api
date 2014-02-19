# feincms-pages-api [![Build Status](https://travis-ci.org/incuna/feincms-pages-api.png?branch=master)](https://travis-ci.org/incuna/feincms-pages-api)
Custom [FeinCMS](https://github.com/feincms/feincms) pages with navigations exposed through the [Django Rest framework](https://github.com/tomchristie/django-rest-framework/tree/master).

##Installation

    pip install feincms-pages-api


In `settings.py`

    INSTALLED_APPS = (
        ...
        'pages.api',
        ...
    ),


In your `urls.py`

    urlpatterns = patterns('',
        url(r'', include(
            patterns('',
                url(r'', include('pages.api.urls.page')),
                url(r'', include('pages.api.urls.page_group')),
            ),
            namespace='pages',
        ))
    )
