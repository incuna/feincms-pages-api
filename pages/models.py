from django.db import models
from django.utils.translation import ugettext_lazy as _
from feincms.models import Base
from orderable.models import Orderable
from rest_framework.reverse import reverse


class Page(Base):
    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255, unique=True)

    def get_absolute_url(self, request=None):
        """
        Returns the absolute url.

        If a request is passed the url will include the domain and port.
        """
        return reverse('pages:page-detail', kwargs={'pk': self.pk}, request=request)

    def __str__(self):
        return self.name


class Group(models.Model):
    slug = models.SlugField(_('slug'), max_length=255, unique=True)

    def __str__(self):
        return self.slug

    def get_absolute_url(self, request=None):
        return reverse(
            'pages:group-detail', kwargs={'slug': self.slug}, request=request)


class GroupItem(Orderable):
    page = models.ForeignKey(Page)
    group = models.ForeignKey(Group)
