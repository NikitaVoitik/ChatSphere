# Generated by Django 5.1.4 on 2025-01-01 19:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiMeta', '0003_apikey_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='apikey',
            unique_together={('user', 'model')},
        ),
    ]
