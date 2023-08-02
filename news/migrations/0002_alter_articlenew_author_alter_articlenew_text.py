# Generated by Django 4.2.2 on 2023-08-02 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlenew',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article_new_object', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='articlenew',
            name='text',
            field=models.TextField(),
        ),
    ]
