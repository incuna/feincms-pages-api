from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from feincms_extensions.content_types import JsonRichTextContent
from user_management.models.mixins import ActiveUserMixin, BasicUserFieldsMixin

from pages.models import Page


class User(ActiveUserMixin, BasicUserFieldsMixin, PermissionsMixin, AbstractBaseUser):
    pass


Page.register_regions(
    ('abstract', 'Abstract/Summary'),
    ('body', 'Main Article'),
)
Page.create_content_type(JsonRichTextContent)
Page.register_extensions(
    'feincms_extensions.render_regions',
    'feincms_extensions.render_json',
)
