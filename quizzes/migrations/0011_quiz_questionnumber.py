# Generated by Django 4.1 on 2022-09-06 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0010_answer_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='questionNumber',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]