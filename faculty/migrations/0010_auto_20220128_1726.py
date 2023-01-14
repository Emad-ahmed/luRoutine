# Generated by Django 3.2.9 on 2022-01-28 11:26

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0009_auto_20220116_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='pre_req',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dependents', to='faculty.course', verbose_name='Pre Req'),
        ),
        migrations.AlterField(
            model_name='departmenthead',
            name='date_of_joining',
            field=models.DateField(default=datetime.datetime(2022, 1, 28, 11, 26, 56, 641996, tzinfo=utc), verbose_name='Date of Joining'),
        ),
        migrations.AlterField(
            model_name='facultydean',
            name='date_of_joining',
            field=models.DateField(default=datetime.datetime(2022, 1, 28, 11, 26, 56, 640971, tzinfo=utc), verbose_name='Date of Joining'),
        ),
    ]
