# Generated by Django 3.2.9 on 2022-02-21 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0016_auto_20220221_2331'),
        ('student', '0002_auto_20220113_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='curriculum',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='batches', to='faculty.curriculum', verbose_name='Curriculum'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='batch',
            name='start_effect_date',
            field=models.DateField(null=True, verbose_name='Start Effect Date'),
        ),
    ]
