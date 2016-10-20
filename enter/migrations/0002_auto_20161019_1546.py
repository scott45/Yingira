# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Name', models.CharField(max_length=30)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='products',
            name='Department',
        ),
        migrations.RemoveField(
            model_name='store',
            name='store_logo',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
