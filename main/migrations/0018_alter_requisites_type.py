# Generated by Django 4.0.2 on 2022-03-11 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_requisites_hide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisites',
            name='type',
            field=models.CharField(blank=True, default='', max_length=300, verbose_name='Тип'),
        ),
    ]