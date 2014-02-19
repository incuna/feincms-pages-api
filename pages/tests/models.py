from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from feincms.content.richtext.models import RichTextContent
from user_management.models.mixins import ActiveUserMixin

from pages.models import Page


class User(ActiveUserMixin, PermissionsMixin, AbstractBaseUser):
    pass


Page.register_regions(
    ('abstract', 'Abstract/Summary'),
    ('body', 'Main Article'),
)
Page.create_content_type(RichTextContent)
Page.register_extensions(
    'pages.extensions.render_regions',
)
