# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
        ('cmsplugin_randomquote', '0002_randomquoteplugin'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleQuotePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, to='cms.CMSPlugin', primary_key=True)),
                ('quote', models.ForeignKey(to='cmsplugin_randomquote.Quote')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
