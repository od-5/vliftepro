# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setup',
            name='phone',
            field=models.CharField(max_length=256, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d', blank=True),
            preserve_default=True,
        ),
    ]
