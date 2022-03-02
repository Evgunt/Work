# Generated by Django 4.0.2 on 2022-03-02 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_checks_docs_alter_checks_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checks',
            name='docs',
            field=models.FileField(blank=True, default='', upload_to='', verbose_name='Документ'),
        ),
        migrations.AlterField(
            model_name='checks',
            name='pay',
            field=models.FileField(blank=True, default='', upload_to='', verbose_name='Загрузить платежное поручение'),
        ),
        migrations.AlterField(
            model_name='checks',
            name='upd',
            field=models.FileField(blank=True, default='', upload_to='', verbose_name='УПД'),
        ),
    ]