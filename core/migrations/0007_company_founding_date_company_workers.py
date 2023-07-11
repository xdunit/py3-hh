# Generated by Django 4.2.2 on 2023-07-06 16:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0003_resume'),
        ('core', '0006_alter_vacancy_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='founding_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='workers',
            field=models.ManyToManyField(to='worker.worker'),
        ),
    ]