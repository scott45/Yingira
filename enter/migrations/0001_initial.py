# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=30)),
                ('store_logo', models.FileField(upload_to='')),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('Names', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='store',
            name='Owner',
            field=models.ForeignKey(to='enter.User'),
        ),
        migrations.AddField(
            model_name='products',
            name='Department',
            field=models.ForeignKey(to='enter.Store'),
        ),
    ]
