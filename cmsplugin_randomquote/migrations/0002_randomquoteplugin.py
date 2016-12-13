# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('cmsplugin_randomquote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RandomQuotePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='cms.CMSPlugin', auto_created=True, serialize=False)),
                ('amount', models.IntegerField(default=1, help_text='The number of random quotes to be displayed.')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
