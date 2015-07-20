# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u0413\u043e\u0440\u043e\u0434')),
                ('lift', models.DecimalField(verbose_name='\u041a\u043e\u043b-\u0432\u043e \u043b\u0438\u0444\u0442\u043e\u0432', max_digits=5, decimal_places=0)),
                ('slug', models.SlugField(max_length=100, verbose_name='url', blank=True)),
            ],
            options={
                'verbose_name': '\u0413\u043e\u0440\u043e\u0434\u0430',
                'verbose_name_plural': '\u0413\u043e\u0440\u043e\u0434\u0430',
            },
            bases=(models.Model,),
        ),
    ]
