# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0007_auto_20150722_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='coord_x',
            field=models.DecimalField(decimal_places=6, editable=False, max_digits=8, blank=True, null=True, verbose_name='\u0428\u0438\u0440\u0438\u043d\u0430'),
        ),
        migrations.AlterField(
            model_name='address',
            name='coord_y',
            field=models.DecimalField(decimal_places=6, editable=False, max_digits=8, blank=True, null=True, verbose_name='\u0414\u043e\u043b\u0433\u043e\u0442\u0430'),
        ),
    ]
