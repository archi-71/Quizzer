# Generated by Django 4.1 on 2022-09-06 00:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0007_remove_question_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='likes',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
