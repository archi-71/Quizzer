# Generated by Django 4.1 on 2022-09-08 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0014_rename_results_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='correctAnswers',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='incorrectAnswers',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
