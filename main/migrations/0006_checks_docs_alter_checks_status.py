# Generated by Django 4.0.2 on 2022-03-02 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_adress_requisites_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='checks',
            name='docs',
            field=models.FileField(default='', upload_to='', verbose_name='Документ'),
        ),
        migrations.AlterField(
            model_name='checks',
            name='status',
            field=models.CharField(default='', max_length=300, verbose_name='Статус'),
        ),
    ]
