# Generated by Django 3.2.9 on 2022-02-26 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_remove_batch_start_effect_date'),
        ('semester', '0005_auto_20220226_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='MergedSectionDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('starting_id', models.CharField(default='*', max_length=16, verbose_name='Starting ID')),
                ('ending_id', models.CharField(default='*', max_length=16, verbose_name='Ending ID')),
                ('distribution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='merged_section_details', to='semester.coursedistribution', verbose_name='Distributed Course')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='merged_section_details', to='student.section', verbose_name='Section')),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
    ]
