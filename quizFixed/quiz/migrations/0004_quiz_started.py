# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-15 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_round_round_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='started',
            field=models.BooleanField(default=False),
        ),
    ]