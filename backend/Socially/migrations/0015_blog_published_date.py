# Generated by Django 3.2.23 on 2024-01-19 06:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Socially', '0014_remove_blog_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 19, 6, 45, 20, 392236, tzinfo=utc), null=True),
        ),
    ]
