# Generated by Django 3.2.9 on 2021-12-01 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('department_id', models.CharField(max_length=32, unique=True, verbose_name='Short Code')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('head', models.CharField(max_length=255, verbose_name='Head of Department')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('dean', models.CharField(max_length=255, verbose_name='Dean of Faculty')),
            ],
            options={
                'verbose_name': 'Faculty',
                'verbose_name_plural': 'Faculties',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('teacher_id', models.CharField(max_length=255, verbose_name='Teacher ID')),
                ('first_name', models.CharField(max_length=128, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=128, verbose_name='Last Name')),
                ('name_initials', models.CharField(max_length=32, unique=True, verbose_name='Name Initials')),
                ('designation', models.CharField(max_length=255, verbose_name='Designation')),
                ('type', models.CharField(choices=[('permanent', 'Permanent'), ('other', 'other')], default='permanent', max_length=12, verbose_name='Faculty Type')),
                ('contact_number', models.CharField(max_length=20, verbose_name='Contact Number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('contact_hour', models.FloatField(verbose_name='Contact Hour')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teachers', to='faculty.department', verbose_name='Department')),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('program_id', models.CharField(max_length=32, unique=True, verbose_name='Short Code')),
                ('title', models.CharField(max_length=255, verbose_name='Program')),
                ('total_credit', models.FloatField(verbose_name='Total Credit')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='programs', to='faculty.department', verbose_name='Department')),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='departments', to='faculty.faculty', verbose_name='Faculty'),
        ),
    ]
