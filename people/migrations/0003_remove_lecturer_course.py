# Generated by Django 3.0.2 on 2020-01-18 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20200118_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='course',
        ),
    ]
