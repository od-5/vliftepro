# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0006_cityslider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='coord_x',
            field=models.DecimalField(null=True, verbose_name='\u0428\u0438\u0440\u0438\u043d\u0430', max_digits=8, decimal_places=6, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='coord_y',
            field=models.DecimalField(null=True, verbose_name='\u0414\u043e\u043b\u0433\u043e\u0442\u0430', max_digits=8, decimal_places=6, blank=True),
        ),
    ]
