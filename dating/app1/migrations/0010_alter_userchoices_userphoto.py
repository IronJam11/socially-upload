# Generated by Django 3.2.23 on 2024-01-29 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_messages_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userchoices',
            name='userphoto',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
