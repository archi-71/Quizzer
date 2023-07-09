# Generated by Django 4.1 on 2022-09-11 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0019_user_averagescore_user_bestcategory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='averageScore',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='bestCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='best', to='quizzes.category'),
        ),
        migrations.AlterField(
            model_name='user',
            name='worstCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='worst', to='quizzes.category'),
        ),
    ]
