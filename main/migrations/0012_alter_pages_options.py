# Generated by Django 3.2.10 on 2022-01-10 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_pages_index'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pages',
            options={'ordering': ['index'], 'verbose_name': 'Блок сайта', 'verbose_name_plural': 'Блоки сайта'},
        ),
    ]
