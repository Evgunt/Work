# Generated by Django 4.0.2 on 2022-03-06 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_helpmessage_options_alter_helpmessage_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checks',
            name='docs',
            field=models.FileField(blank=True, default='', upload_to='media/checks', verbose_name='Документ'),
        ),
        migrations.AlterField(
            model_name='checks',
            name='pay',
            field=models.FileField(blank=True, default='', upload_to='media/checks', verbose_name='Загрузить платежное поручение'),
        ),
        migrations.AlterField(
            model_name='checks',
            name='upd',
            field=models.FileField(blank=True, default='', upload_to='media/checks', verbose_name='УПД'),
        ),
        migrations.CreateModel(
            name='Files_helps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='contact', verbose_name='Файл')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.helpmessage')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
    ]
