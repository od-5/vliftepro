# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u0417\u0434\u0430\u043d\u0438\u0435', blank=True)),
                ('address', models.CharField(max_length=100, verbose_name='\u0410\u0434\u0440\u0435\u0441')),
                ('coord_x', models.DecimalField(decimal_places=6, editable=False, max_digits=8, blank=True, null=True, verbose_name='\u0428\u0438\u0440\u0438\u043d\u0430')),
                ('coord_y', models.DecimalField(decimal_places=6, editable=False, max_digits=8, blank=True, null=True, verbose_name='\u0414\u043e\u043b\u0433\u043e\u0442\u0430')),
                ('city', models.ForeignKey(verbose_name='\u0413\u043e\u0440\u043e\u0434', to='city.City')),
            ],
            options={
                'verbose_name': '\u0410\u0434\u0440\u0435\u0441',
                'verbose_name_plural': '\u0410\u0434\u0440\u0435\u0441\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': '\u0413\u043e\u0440\u043e\u0434', 'verbose_name_plural': '\u0413\u043e\u0440\u043e\u0434\u0430'},
        ),
    ]
