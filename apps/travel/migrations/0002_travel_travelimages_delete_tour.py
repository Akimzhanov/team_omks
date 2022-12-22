# Generated by Django 4.1.4 on 2022-12-22 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('phone_number', models.CharField(default='+996', max_length=30)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateTimeField()),
                ('transport', models.CharField(max_length=50)),
                ('living', models.TextField(max_length=100)),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TravelImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='travel_images/carousel')),
                ('travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travel_images', to='travel.travel')),
            ],
        ),
        migrations.DeleteModel(
            name='Tour',
        ),
    ]
