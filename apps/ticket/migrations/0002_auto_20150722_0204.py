# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='email',
        ),
        migrations.AddField(
            model_name='ticket',
            name='phone',
            field=models.EmailField(default='', max_length=256, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='text',
            field=models.TextField(null=True, verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f', blank=True),
            preserve_default=True,
        ),
    ]
