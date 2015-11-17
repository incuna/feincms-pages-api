# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import user_management.models.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='date joined')),
                ('email', models.EmailField(unique=True, verbose_name='Email address', max_length=511)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('name', models.CharField(verbose_name='Name', max_length=255)),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('groups', models.ManyToManyField(related_query_name='user', blank=True, to='auth.Group', related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', blank=True, to='auth.Permission', related_name='user_set', help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            bases=(user_management.models.mixins.NameUserMethodsMixin, models.Model),
        ),
    ]
