# Generated by Django 5.1.3 on 2024-11-12 15:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='CreadoEn',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]