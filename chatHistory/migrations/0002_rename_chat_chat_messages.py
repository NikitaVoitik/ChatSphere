# Generated by Django 5.1.4 on 2025-01-04 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatHistory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='chat',
            new_name='messages',
        ),
    ]
