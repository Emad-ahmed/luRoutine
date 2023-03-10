# Generated by Django 3.2.9 on 2022-02-21 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0014_auto_20220206_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('start_effect_date', models.DateField(verbose_name='Start Effect Date')),
                ('end_effect_date', models.DateField(verbose_name='End Effect Date')),
                ('active', models.BooleanField(verbose_name='Active')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curriculums', to='faculty.program', verbose_name='Program')),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='course',
            name='curriculum',
            field=models.ManyToManyField(related_name='courses', to='faculty.Curriculum', verbose_name='Curriculum'),
        ),
    ]
