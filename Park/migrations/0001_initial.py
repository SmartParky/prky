# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-03-11 17:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('capacity', models.PositiveSmallIntegerField(verbose_name='Capacity')),
                ('address', models.TextField(blank=True, verbose_name='Address')),
                ('number_of_car_inside', models.PositiveSmallIntegerField(verbose_name='Number of Car')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('coordinate', geoposition.fields.GeopositionField(blank=True, max_length=42, null=True, verbose_name='Coordinate')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.City', verbose_name='City')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Users')),
            ],
            options={
                'verbose_name': 'Park',
                'verbose_name_plural': 'Parks',
            },
        ),
    ]
