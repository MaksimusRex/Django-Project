# Generated by Django 5.1.2 on 2024-11-30 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0003_alter_criminalmaininfo_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='criminalmaininfo',
            old_name='approved',
            new_name='is_approved',
        ),
    ]