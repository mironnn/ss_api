# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('archive', models.BooleanField(default=False)),
                ('cost', models.DecimalField(decimal_places=5, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('preferences', models.CharField(choices=[('PC', 'Computer'), ('TV', 'TV')], max_length=2)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='advert',
            name='topic',
            field=models.ManyToManyField(to='models_first.Topic'),
        ),
        migrations.AddField(
            model_name='advert',
            name='user',
            field=models.ManyToManyField(to='models_first.Client'),
        ),
    ]
