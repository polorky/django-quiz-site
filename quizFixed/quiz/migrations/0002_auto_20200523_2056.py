# Generated by Django 3.0.5 on 2020-05-23 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='pic_round',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='round',
            name='picture1',
            field=models.ImageField(blank=True, upload_to='quiz_pics'),
        ),
        migrations.AddField(
            model_name='round',
            name='picture10',
            field=models.ImageField(blank=True, upload_to='quiz_pics'),
        ),
        migrations.AddField(
            model_name='round',
            name='picture2',
            field=models.ImageField(blank=True, upload_to='quiz_pics'),
        ),
        migrations.AddField(
            model_name='round',
            name='picture3',
            field=models.ImageField(blank=True, upload_to='quiz_pics'),
        ),
        migrations.AddField(
            model_name='round',
            name='picture4',
            field=models.ImageField(blank=True, upload_to='quiz_pics'),
        ),
        migrations.AddField(
            model_name='round',
            name='picture5',
            field=models.ImageField(blank=True, upload_to='quiz_pics'),
        ),
        migrations.AddField(
            model_name='round',
            name='picture6',
            field=models.ImageField(blank=True, upload_to='quiz_pics'),
        ),
        migrations.AddField(
            model_name='round',
            name='picture7',
            field=models.ImageField(blank=True, upload_to='quiz_pics'),
        ),
        migrations.AddField(
            model_name='round',
            name='picture8',
            field=models.ImageField(blank=True, upload_to='quiz_pics'),
        ),
        migrations.AddField(
            model_name='round',
            name='picture9',
            field=models.ImageField(blank=True, upload_to='quiz_pics'),
        ),
    ]