# Generated by Django 3.0.2 on 2020-01-18 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('code', models.CharField(max_length=5, unique=True)),
                ('category', models.CharField(choices=[(1, 'Geology'), (2, 'Geophysics'), (3, 'Others')], max_length=2)),
                ('units', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('drive_link', models.URLField()),
            ],
        ),
    ]
