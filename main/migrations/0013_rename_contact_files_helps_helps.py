# Generated by Django 4.0.2 on 2022-03-06 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_checks_docs_alter_checks_pay_alter_checks_upd_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='files_helps',
            old_name='contact',
            new_name='helps',
        ),
    ]
