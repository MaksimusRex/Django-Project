# Generated by Django 5.1.2 on 2024-12-09 18:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('criminals', '0009_criminalmaininfo_prison'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(choices=[('Car', 'Car'), ('Motorcycle', 'Motorcycle'), ('Truck', 'Truck'), ('Van', 'Van'), ('Other', 'Other')], default='Other', max_length=20)),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField()),
                ('license_plate', models.CharField(max_length=15, unique=True)),
                ('color', models.CharField(blank=True, max_length=30, null=True)),
                ('criminal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='criminals.criminalmaininfo')),
            ],
        ),
    ]
