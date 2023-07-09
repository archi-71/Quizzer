# Generated by Django 4.1 on 2022-09-02 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='averageScore',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='quizzesCompleted',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='quizzesCreated',
            field=models.IntegerField(default=0),
        ),
    ]
