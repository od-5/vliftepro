# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_setup_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setup',
            name='video',
        ),
    ]
