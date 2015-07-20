# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.page.common


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0005_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='CitySlider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0438 \u0430\u0434\u0440\u0435\u0441 \u043e\u0431\u044a\u0435\u043a\u0442\u0430')),
                ('type', models.CharField(max_length=255, null=True, verbose_name='\u041a\u043b\u0430\u0441\u0441', blank=True)),
                ('lift', models.IntegerField(default=1, null=True, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043b\u0438\u0444\u0442\u043e\u0432', blank=True)),
                ('floor', models.IntegerField(default=1, null=True, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u044d\u0442\u0430\u0436\u0435\u0439', blank=True)),
                ('maneuverability', models.IntegerField(default=1, null=True, verbose_name='\u041f\u0440\u0438\u043c\u0435\u0440\u043d\u0430\u044f \u043f\u0440\u043e\u0445\u043e\u0434\u0438\u043c\u043e\u0441\u0442\u044c \u0435\u0436\u0435\u0434\u043d\u0435\u0432\u043d\u043e', blank=True)),
                ('image', models.ImageField(upload_to=apps.page.common.get_slider_path, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('city', models.ForeignKey(verbose_name='\u0413\u043e\u0440\u043e\u0434', to='city.City')),
            ],
            options={
                'verbose_name': '\u0411\u0438\u0437\u043d\u0435\u0441 \u0446\u0435\u043d\u0442\u0440',
                'verbose_name_plural': '\u0411\u0438\u0437\u043d\u0435\u0441 \u0446\u0435\u043d\u0442\u0440\u044b',
            },
            bases=(models.Model,),
        ),
    ]
