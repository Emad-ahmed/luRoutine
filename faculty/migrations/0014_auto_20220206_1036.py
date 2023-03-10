# Generated by Django 3.2.9 on 2022-02-06 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0013_auto_20220128_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(max_length=16, unique=True, verbose_name='Course Code'),
        ),
        migrations.AlterField(
            model_name='department',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Title'),
        ),
    ]
