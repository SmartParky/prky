# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-03-07 12:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('admin', 'Admin'), ('customer', 'Customer'), ('park-owner', 'Park Owner')], default='customer', max_length=50, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Telefon numarası formatı şu şekilde olmalıdır: '05xx-xxx-xx-xx'.", regex='^(05(\\d{2})-(\\d{3})-(\\d{2})-(\\d{2}))$')], verbose_name='Phone Number'),
        ),
    ]
