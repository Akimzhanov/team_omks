# Generated by Django 4.1.4 on 2022-12-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartphones', '0002_alter_brand_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, primary_key=True, serialize=False),
        ),
    ]
