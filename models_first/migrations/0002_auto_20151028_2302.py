# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('models_first', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='user',
        ),
        migrations.AddField(
            model_name='advert',
            name='user',
            field=models.ForeignKey(default=1976, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
