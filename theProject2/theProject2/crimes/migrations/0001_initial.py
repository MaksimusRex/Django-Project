# Generated by Django 5.1.2 on 2024-12-09 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('criminals', '0009_criminalmaininfo_prison'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('points', models.PositiveIntegerField()),
                ('crime_type', models.CharField(choices=[('INF', 'Infraction'), ('MIS', 'Misdemeanor'), ('FM', 'Felony-Misdemeanor'), ('FEL', 'Felony')], max_length=3)),
                ('criminal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crimes', to='criminals.criminalmaininfo')),
            ],
        ),
    ]