# Generated by Django 4.1.7 on 2023-04-26 12:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_alter_blog_created_alter_blog_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 26, 17, 35, 38, 604843)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 26, 17, 35, 38, 604843)),
        ),
    ]
