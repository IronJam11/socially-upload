# Generated by Django 3.2.23 on 2024-01-23 16:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Socially', '0020_auto_20240120_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 23, 16, 38, 36, 483709, tzinfo=utc), null=True),
        ),
    ]
