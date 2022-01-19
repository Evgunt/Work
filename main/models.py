from django.contrib import admin
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from .utilities import get_timestamp_path
from ckeditor.fields import RichTextField


class slider(models.Model):
    title = models.CharField(max_length=300, default="", blank=False, verbose_name='Заголовок слайда')
    content = models.TextField(default="", blank=True, verbose_name='Текст слайда')
    image = models.ImageField(blank=False, upload_to=get_timestamp_path, verbose_name='Изображение', default="", help_text="Минимальный размер 1300x200px")

    class Meta:
        verbose_name_plural = 'Слайдер'
        verbose_name = 'Слайдер'

    def __str__(self):
        return self.title


class services(models.Model):
    title = models.CharField(max_length=300, default="", blank=False, verbose_name='Заголовок товара')
    content = RichTextField(default="", blank=True, verbose_name='Текст товара')
    price = models.IntegerField(default=0, blank=False, verbose_name='Цена товара')

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def __str__(self):
        return self.title


class photos(models.Model):
    parent = models.ForeignKey(services, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(blank=False, upload_to=get_timestamp_path, verbose_name='Изображение', default="", help_text="Минимальный размер 160x160px")

    class Meta:
        verbose_name_plural = 'Изображения товара'
        verbose_name = 'Изображение товара'


class pages(models.Model):
    title = models.CharField(max_length=300, default="", blank=False, verbose_name='Заголовок товара')
    content = RichTextField(default="", blank=True, verbose_name='Текст товара')
    index = models.IntegerField(default=0, blank=False, verbose_name='Индекс сортировки', help_text="Порядок блоков на сайте (от 0 до ...)")

    class Meta:
        verbose_name_plural = 'Блоки сайта'
        verbose_name = 'Блок сайта'
        ordering = ['index']

    def __str__(self):
        return self.title


class gallery(models.Model):
    alt = models.CharField(max_length=300, default="", blank=False, verbose_name='alt Изображения')
    image = models.ImageField(blank=False, upload_to=get_timestamp_path, verbose_name='Изображение', default="", help_text="Минимальный размер 455x455px")

    class Meta:
        verbose_name_plural = 'Галерея сайта'
        verbose_name = 'Галерея сайта'

    def __str__(self):
        return self.alt


class firstBlock(models.Model):
    title = models.CharField(max_length=300, default="", blank=False, verbose_name='Заголовок')
    content = RichTextField(default="", blank=False, verbose_name='Текст')

    class Meta:
        verbose_name_plural = 'Блок описания'
        verbose_name = 'Блок описания'

    def __str__(self):
        return self.title