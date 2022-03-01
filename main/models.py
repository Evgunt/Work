from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    send_messages = models.BooleanField(default=True, verbose_name='Уведомления')
    phone = models.CharField(default="", max_length=300, verbose_name='Телефон')
    region = models.CharField(default="", max_length=300, verbose_name='Region')
    time = models.CharField(default="", max_length=300, verbose_name='Часовой пояс')
    language = models.CharField(default="", max_length=300, verbose_name='Язык')
    personal = models.BooleanField(default=True, blank=False)
    key = models.CharField(default="", max_length=300)

    class Meta(AbstractUser.Meta):
        pass


class tariffs(models.Model):
    name = models.CharField(unique=True, max_length=300, default="", blank=False, verbose_name='Название')
    price1 = models.CharField(max_length=300, default="", blank=True, verbose_name='Цена (1 месяц)')
    price2 = models.CharField(max_length=300, default="", blank=True, verbose_name='Цена (3 месяца)')
    price3 = models.CharField(max_length=300, default="", blank=True, verbose_name='Цена (12 месяцев)')
    content = RichTextField(default="", blank=True, verbose_name='Преимущества')

    class Meta:
        verbose_name_plural = 'Тарифы'
        verbose_name = 'Тариф'

    def __str__(self):
        return self.name


class keys(models.Model):
    number = models.CharField(max_length=300, default="", blank=False, verbose_name='Номер ключа')
    name = models.CharField(max_length=300, default="", blank=True, verbose_name='Название')
    tariff = models.ForeignKey(tariffs, blank=True, verbose_name='Тариф',
                               on_delete=models.PROTECT, to_field="name")
    date = models.DateField(editable=True, auto_now=False, db_index=True, blank=True, verbose_name='Работает до')
    owner = models.ForeignKey(AdvUser, on_delete=models.CASCADE, blank=False,
                              verbose_name='Владелец', to_field="username")
    checkNum = models.CharField(max_length=300, default="", blank=True, verbose_name='Проверочный код')

    class Meta:
        verbose_name_plural = 'Ключи'
        verbose_name = 'Ключь'

    def __str__(self):
        return self.number


class requisites(models.Model):
    org = models.CharField(max_length=300, default="", blank=False, verbose_name='Тип организации')
    inn = models.CharField(max_length=300, default="", blank=False, verbose_name='ИНН')
    kpp = models.CharField(max_length=300, default="", blank=False, verbose_name='КПП')
    company = models.CharField(max_length=300, default="", blank=False, verbose_name='Юридическое название организации')
    adress = models.CharField(max_length=300, default="", blank=False, verbose_name='Юридический адрес')
    contacts = models.CharField(max_length=300, default="", blank=False, verbose_name='Контактное лицо')
    email = models.CharField(max_length=300, default="", blank=False, verbose_name='E-mail')
    phone = models.CharField(max_length=300, default="", blank=False, verbose_name='Контактный телефон')
    docs = models.CharField(max_length=300, default="", blank=False, verbose_name='Как будет забирать документы')
    bank = models.CharField(max_length=300, default="", blank=False, verbose_name='Наименование банка')
    checking = models.CharField(max_length=300, default="", blank=False, verbose_name='Расчетный счет')
    bic = models.CharField(max_length=300, default="", blank=False, verbose_name='БИК')
    checkingCo = models.CharField(max_length=300, default="", blank=False, verbose_name='Корреспондентский счет')
    ogrn = models.CharField(max_length=300, default="", blank=False, verbose_name='ОГРН')

    class Meta:
        verbose_name_plural = 'Реквизиты'
        verbose_name = 'Реквизит'

    def __str__(self):
        return self.company
