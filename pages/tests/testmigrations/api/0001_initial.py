# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import user_management.api.models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthToken',
            fields=[
                ('key', models.CharField(serialize=False, max_length=40, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('expires', models.DateTimeField(default=user_management.api.models.update_expiry, editable=False)),
                ('user', models.ForeignKey(related_name='authtoken', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
