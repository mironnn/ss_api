# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_first', '0002_auto_20151028_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
