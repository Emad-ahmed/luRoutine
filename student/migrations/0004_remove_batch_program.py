# Generated by Django 3.2.9 on 2022-02-22 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20220221_2331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='program',
        ),
    ]
