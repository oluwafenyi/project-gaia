# Generated by Django 3.0.2 on 2020-01-20 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_remove_lecturer_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='executive',
            name='instagram',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='executive',
            name='twitter',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='executive',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
