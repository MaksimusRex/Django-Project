# Generated by Django 5.1.2 on 2024-12-10 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prisons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prison',
            name='picture',
            field=models.URLField(blank=True, null=True),
        ),
    ]
