# Generated by Django 3.2.10 on 2022-01-10 05:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_firstblock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstblock',
            name='content',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Текст'),
        ),
    ]
