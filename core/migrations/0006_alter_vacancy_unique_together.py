# Generated by Django 4.2.2 on 2023-07-04 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_category_alter_vacancy_options_vacancy_category'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vacancy',
            unique_together={('title', 'email')},
        ),
    ]
