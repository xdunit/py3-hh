# Generated by Django 4.2.2 on 2023-06-22 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('employees_num', models.SmallIntegerField()),
                ('is_hunting', models.BooleanField(default=True, verbose_name='Есть вакансии?')),
            ],
        ),
    ]
