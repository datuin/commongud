# Generated by Django 2.2.6 on 2020-12-27 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gud_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='field_name',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
