# Generated by Django 5.1.2 on 2024-12-01 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0004_rename_approved_criminalmaininfo_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='criminalmaininfo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]
