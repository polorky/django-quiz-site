# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-15 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_round_quiz_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='round',
            name='quiz_number',
        ),
        migrations.AddField(
            model_name='answer',
            name='quiz_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
