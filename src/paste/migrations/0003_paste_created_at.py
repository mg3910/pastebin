# Generated by Django 5.1.6 on 2025-02-19 12:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0002_remove_paste_id_paste_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='paste',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
