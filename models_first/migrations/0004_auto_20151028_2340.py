# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_first', '0003_auto_20151028_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='topic',
            field=models.ManyToManyField(blank=True, to='models_first.Topic'),
        ),
    ]
