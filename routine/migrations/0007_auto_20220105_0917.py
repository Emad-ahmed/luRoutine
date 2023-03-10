# Generated by Django 3.2.9 on 2022-01-05 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0006_remove_building_established_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlotDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('start_time', models.TimeField(verbose_name='Start Time')),
                ('end_time', models.TimeField(verbose_name='End Time')),
            ],
            options={
                'verbose_name': 'Slot Detail',
                'verbose_name_plural': 'Slot Details',
            },
        ),
        migrations.CreateModel(
            name='SlotMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=128, verbose_name='Title')),
                ('start_effect_date', models.DateField(verbose_name='Start Effect Date')),
                ('end_effect_date', models.DateField(verbose_name='End Effect Date')),
                ('short_description', models.TextField(blank=True, verbose_name='Short Description')),
                ('status', models.CharField(max_length=128, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Slot Master',
                'verbose_name_plural': 'Slot Masters',
            },
        ),
        migrations.DeleteModel(
            name='Slot',
        ),
        migrations.AddField(
            model_name='slotdetail',
            name='slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='routine.slotmaster', verbose_name='Slot'),
        ),
    ]
