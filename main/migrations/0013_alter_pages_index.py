# Generated by Django 3.2.10 on 2022-01-10 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_pages_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='index',
            field=models.IntegerField(default=0, help_text='Порядок блоков на сайте (от 0 до ...)', verbose_name='Индекс сортировки'),
        ),
    ]