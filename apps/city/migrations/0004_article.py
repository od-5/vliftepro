# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0003_format'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('city', models.ForeignKey(verbose_name='\u0413\u043e\u0440\u043e\u0434', to='city.City')),
            ],
            options={
                'verbose_name': '\u0422\u0435\u043a\u0441\u0442',
                'verbose_name_plural': '\u0422\u0435\u043a\u0441\u0442\u0430',
            },
            bases=(models.Model,),
        ),
    ]
