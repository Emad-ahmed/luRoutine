# Generated by Django 3.2.9 on 2023-02-26 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0023_auto_20230215_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_id',
            field=models.CharField(max_length=32, verbose_name='Short Code'),
        ),
        migrations.AlterField(
            model_name='department',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
    ]
