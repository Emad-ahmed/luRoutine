# Generated by Django 3.2.9 on 2022-01-13 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batch',
            options={'verbose_name': 'Batch', 'verbose_name_plural': 'Batches'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': 'Section', 'verbose_name_plural': 'Sections'},
        ),
        migrations.RemoveField(
            model_name='batch',
            name='batch_code',
        ),
    ]
