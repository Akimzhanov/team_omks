# Generated by Django 4.1.4 on 2022-12-22 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartphones', '0003_alter_brand_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphone',
            name='image',
        ),
    ]
