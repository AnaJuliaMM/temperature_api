# Generated by Django 5.0.1 on 2024-02-05 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TemperatureForecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('atmospheric_pressure', models.FloatField()),
                ('humidity', models.FloatField()),
                ('precipitation_percentage', models.FloatField()),
                ('weather_conditions', models.CharField(max_length=150)),
                ('date_tiime', models.DateTimeField()),
            ],
        ),
    ]