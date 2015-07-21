# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0008_auto_20150722_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='meta_desc',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 META_DESCRIPTION', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='meta_key',
            field=models.TextField(null=True, verbose_name='\u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430 META_KEYWORDS', blank=True),
            preserve_default=True,
        ),
    ]
