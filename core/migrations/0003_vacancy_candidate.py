# Generated by Django 4.2.2 on 2023-06-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0002_worker_user_comment'),
        ('core', '0002_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='candidate',
            field=models.ManyToManyField(blank=True, to='worker.worker'),
        ),
    ]
