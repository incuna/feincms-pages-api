# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import feincms.translations
import feincms.extensions


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('slug', models.SlugField(max_length=150, verbose_name='slug')),
                ('parent', models.ForeignKey(blank=True, null=True, to='feincms.Category', verbose_name='parent', related_name='children')),
            ],
            options={
                'ordering': ['parent__title', 'title'],
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('file', models.FileField(max_length=255, verbose_name='file', upload_to='medialibrary/%Y/%m/')),
                ('type', models.CharField(max_length=12, verbose_name='file type', choices=[('image', 'Image'), ('video', 'Video'), ('audio', 'Audio'), ('pdf', 'PDF document'), ('swf', 'Flash'), ('txt', 'Text'), ('rtf', 'Rich Text'), ('zip', 'Zip archive'), ('doc', 'Microsoft Word'), ('xls', 'Microsoft Excel'), ('ppt', 'Microsoft PowerPoint'), ('other', 'Binary')], editable=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('copyright', models.CharField(max_length=200, blank=True, verbose_name='copyright')),
                ('file_size', models.IntegerField(editable=False, blank=True, null=True, verbose_name='file size')),
                ('categories', models.ManyToManyField(to='feincms.Category', blank=True, verbose_name='categories')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'media file',
                'verbose_name_plural': 'media files',
                'abstract': False,
            },
            bases=(models.Model, feincms.extensions.ExtensionsMixin, feincms.translations.TranslatedObjectMixin),
        ),
        migrations.CreateModel(
            name='MediaFileTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('language_code', models.CharField(max_length=10, default='af', verbose_name='language', choices=[('af', 'Afrikaans'), ('ar', 'Arabic'), ('ast', 'Asturian'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('el', 'Greek'), ('en', 'English'), ('en-au', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('es-ve', 'Venezuelan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ga', 'Irish'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hu', 'Hungarian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('lb', 'Luxembourgish'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('my', 'Burmese'), ('nb', 'Norwegian Bokmal'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('th', 'Thai'), ('tr', 'Turkish'), ('tt', 'Tatar'), ('udm', 'Udmurt'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('vi', 'Vietnamese'), ('zh-cn', 'Simplified Chinese'), ('zh-hans', 'Simplified Chinese'), ('zh-hant', 'Traditional Chinese'), ('zh-tw', 'Traditional Chinese')])),
                ('caption', models.CharField(max_length=200, verbose_name='caption')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('parent', models.ForeignKey(to='feincms.MediaFile', related_name='translations')),
            ],
            options={
                'verbose_name': 'media file translation',
                'verbose_name_plural': 'media file translations',
            },
        ),
        migrations.AlterUniqueTogether(
            name='mediafiletranslation',
            unique_together=set([('parent', 'language_code')]),
        ),
    ]
