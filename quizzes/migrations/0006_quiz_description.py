# Generated by Django 4.1 on 2022-09-04 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0005_alter_question_answers_alter_quiz_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='description',
            field=models.CharField(default='', max_length=2000),
            preserve_default=False,
        ),
    ]
