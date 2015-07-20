# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0002_auto_20150719_0141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u0424\u043e\u0440\u043c\u0430\u0442')),
                ('price', models.DecimalField(verbose_name='\u0426\u0435\u043d\u0430', max_digits=6, decimal_places=0)),
            ],
            options={
                'verbose_name': '\u0426\u0435\u043d\u044b \u0438 \u0444\u043e\u0440\u043c\u0430\u0442\u044b',
                'verbose_name_plural': '\u0426\u0435\u043d\u044b \u0438 \u0444\u043e\u0440\u043c\u0430\u0442\u044b',
            },
            bases=(models.Model,),
        ),
    ]
