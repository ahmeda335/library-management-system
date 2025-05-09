# Generated by Django 5.2 on 2025-04-17 22:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_rename_user_order_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='user',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL),
        ),
    ]
