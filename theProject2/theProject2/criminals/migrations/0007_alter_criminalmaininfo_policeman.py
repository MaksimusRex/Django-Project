# Generated by Django 5.1.2 on 2024-12-01 19:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0006_alter_criminalmaininfo_policeman'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='criminalmaininfo',
            name='policeman',
            field=models.ForeignKey(default=None, limit_choices_to={'role': 'Police Officer'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]