# Generated by Django 3.0.5 on 2020-05-17 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quiz_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(choices=[('NS', 'Not Started'), ('WA', 'Waiting for Answers'), ('SA', 'Showing Answers')], default='NS', max_length=2)),
                ('current_round', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_name', models.CharField(max_length=20)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', models.IntegerField()),
                ('question1', models.CharField(max_length=256)),
                ('true_answer1', models.CharField(max_length=50)),
                ('question2', models.CharField(max_length=256)),
                ('true_answer2', models.CharField(max_length=50)),
                ('question3', models.CharField(max_length=256)),
                ('true_answer3', models.CharField(max_length=50)),
                ('question4', models.CharField(max_length=256)),
                ('true_answer4', models.CharField(max_length=50)),
                ('question5', models.CharField(max_length=256)),
                ('true_answer5', models.CharField(max_length=50)),
                ('question6', models.CharField(max_length=256)),
                ('true_answer6', models.CharField(max_length=50)),
                ('question7', models.CharField(max_length=256)),
                ('true_answer7', models.CharField(max_length=50)),
                ('question8', models.CharField(max_length=256)),
                ('true_answer8', models.CharField(max_length=50)),
                ('question9', models.CharField(max_length=256)),
                ('true_answer9', models.CharField(max_length=50)),
                ('question10', models.CharField(max_length=256)),
                ('true_answer10', models.CharField(max_length=50)),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
                ('answer1', models.CharField(blank=True, max_length=50)),
                ('correct1', models.BooleanField(default=False)),
                ('answer2', models.CharField(blank=True, max_length=50)),
                ('correct2', models.BooleanField(default=False)),
                ('answer3', models.CharField(blank=True, max_length=50)),
                ('correct3', models.BooleanField(default=False)),
                ('answer4', models.CharField(blank=True, max_length=50)),
                ('correct4', models.BooleanField(default=False)),
                ('answer5', models.CharField(blank=True, max_length=50)),
                ('correct5', models.BooleanField(default=False)),
                ('answer6', models.CharField(blank=True, max_length=50)),
                ('correct6', models.BooleanField(default=False)),
                ('answer7', models.CharField(blank=True, max_length=50)),
                ('correct7', models.BooleanField(default=False)),
                ('answer8', models.CharField(blank=True, max_length=50)),
                ('correct8', models.BooleanField(default=False)),
                ('answer9', models.CharField(blank=True, max_length=50)),
                ('correct9', models.BooleanField(default=False)),
                ('answer10', models.CharField(blank=True, max_length=50)),
                ('correct10', models.BooleanField(default=False)),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz')),
            ],
        ),
    ]
