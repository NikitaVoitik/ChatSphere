# Generated by Django 5.1.4 on 2025-01-01 22:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiMeta', '0005_modelinterface_image_generation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelMeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('request_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('text_completions', models.BooleanField(default=False)),
                ('image_generation', models.BooleanField(default=False)),
                ('vision', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='apikey',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='apiMeta.modelmeta'),
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
        migrations.DeleteModel(
            name='ModelInterface',
        ),
    ]
