# Generated by Django 3.1.3 on 2023-09-21 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20230917_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catering',
            name='description',
        ),
    ]
