# Generated by Django 4.2.2 on 2023-07-20 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_vacancy_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='employment_type',
            field=models.CharField(choices=[('full', 'Полный рабочий день'), ('part', 'Частичная занятость'), ('comp', 'Сделанная работа')], default='full', max_length=4),
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='skill_name',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='skill_name',
            field=models.ManyToManyField(blank=True, to='core.skill'),
        ),
    ]
