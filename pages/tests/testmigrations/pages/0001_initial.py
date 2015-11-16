# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import feincms.extensions
import feincms.contrib.richtext


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('slug', models.SlugField(verbose_name='slug', unique=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GroupItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('sort_order', models.IntegerField(blank=True, db_index=True)),
                ('group', models.ForeignKey(to='pages.Group')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JsonRichTextContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('text', feincms.contrib.richtext.RichTextField(verbose_name='text', blank=True)),
                ('region', models.CharField(max_length=255)),
                ('ordering', models.IntegerField(default=0, verbose_name='ordering')),
            ],
            options={
                'verbose_name': 'rich text',
                'verbose_name_plural': 'rich texts',
                'db_table': 'pages_page_jsonrichtextcontent',
                'ordering': ['ordering'],
                'abstract': False,
                'permissions': [],
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='name', max_length=255)),
                ('slug', models.SlugField(verbose_name='slug', unique=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, feincms.extensions.ExtensionsMixin),
        ),
        migrations.AddField(
            model_name='jsonrichtextcontent',
            name='parent',
            field=models.ForeignKey(related_name='jsonrichtextcontent_set', to='pages.Page'),
        ),
        migrations.AddField(
            model_name='groupitem',
            name='page',
            field=models.ForeignKey(to='pages.Page'),
        ),
    ]
