# Generated by Django 4.0.2 on 2022-02-28 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keys',
            old_name='workFor',
            new_name='date',
        ),
    ]
