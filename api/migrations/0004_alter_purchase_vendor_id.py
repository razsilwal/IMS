# Generated by Django 5.1.5 on 2025-02-04 01:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_user_groups_user_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='vendor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.vendor'),
        ),
    ]
