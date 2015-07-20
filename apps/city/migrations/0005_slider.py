# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.page.common


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0004_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u0417\u0434\u0430\u043d\u0438\u0435')),
                ('image', models.ImageField(upload_to=apps.page.common.get_slider_path, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('city', models.ForeignKey(verbose_name='\u0413\u043e\u0440\u043e\u0434', to='city.City')),
            ],
            options={
                'verbose_name': '\u0421\u043b\u0430\u0439\u0434',
                'verbose_name_plural': '\u0421\u043b\u0430\u0439\u0434\u044b',
            },
            bases=(models.Model,),
        ),
    ]
