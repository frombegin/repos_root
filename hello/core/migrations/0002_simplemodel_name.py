# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='simplemodel',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 11, 27, 12, 53, 1, 524000, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
