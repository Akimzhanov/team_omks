# Generated by Django 4.1.4 on 2022-12-23 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_travel_travelimages_delete_tour'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='in_stock',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='travel',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
