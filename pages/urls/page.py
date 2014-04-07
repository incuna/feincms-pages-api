from django.conf.urls import include, url

from rest_framework.routers import SimpleRouter

from .. import views


router = SimpleRouter(trailing_slash=False)
router.register(r'pages', views.PageViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
