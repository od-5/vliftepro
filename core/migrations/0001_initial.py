# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a <TITLE>...</TITLE>', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='e-mail \u0434\u043b\u044f \u043f\u0440\u0438\u0451\u043c\u0430 \u0437\u0430\u044f\u0432\u043e\u043a', blank=True)),
                ('video', models.TextField(null=True, verbose_name='HTML-\u043a\u043e\u0434 \u0432\u0438\u0434\u0435\u043e', blank=True)),
                ('meta_key', models.TextField(verbose_name='\u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430 META_KEYWORDS', blank=True)),
                ('meta_desc', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 META_DESCRIPTION', blank=True)),
                ('top_js', models.TextField(verbose_name='\u0421\u043a\u0440\u0438\u043f\u0442\u044b \u0432 <HEAD>..</HEAD>', blank=True)),
                ('bottom_js', models.TextField(verbose_name='\u0421\u043a\u0440\u0438\u043f\u0442\u044b \u043f\u0435\u0440\u0435\u0434 \u0437\u0430\u043a\u0440\u044b\u0432\u0430\u044e\u0449\u0438\u043c </BODY>', blank=True)),
            ],
            options={
                'verbose_name': '\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0430\u0439\u0442\u0430',
                'verbose_name_plural': '\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0430\u0439\u0442\u0430',
            },
            bases=(models.Model,),
        ),
    ]
