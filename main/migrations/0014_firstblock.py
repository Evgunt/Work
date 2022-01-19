# Generated by Django 3.2.10 on 2022-01-10 05:37

from django.db import migrations, models
import main.utilities


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_pages_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='firstBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=300, verbose_name='Заголовок')),
                ('content', models.TextField(default='', verbose_name='Текст')),
                ('image1', models.ImageField(default='', help_text='Минимальный размер 425x425px', upload_to=main.utilities.get_timestamp_path, verbose_name='Изображение слева')),
                ('image2', models.ImageField(default='', help_text='Минимальный размер 425x425px', upload_to=main.utilities.get_timestamp_path, verbose_name='Изображение справа')),
            ],
            options={
                'verbose_name': 'Блок описания',
                'verbose_name_plural': 'Блок описания',
            },
        ),
    ]
