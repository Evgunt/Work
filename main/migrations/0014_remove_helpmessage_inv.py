# Generated by Django 4.0.2 on 2022-03-06 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_rename_contact_files_helps_helps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helpmessage',
            name='inv',
        ),
    ]
