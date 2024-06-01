from django.conf import settings
from django.db import models


NULLABLE = {'blank': True, 'null': True}

types_sellers = [
    (0, "Завод"),
    (1, "Розничная сеть"),
    (2, "Индивидуальный предприниматель"),
]


class Contacts(models.Model):
    """ Класс модели контактов """

    email = models.EmailField(verbose_name='Электронная почта')
    country = models.CharField(max_length=100, verbose_name='Страна', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    street = models.CharField(max_length=150, verbose_name='Улица', **NULLABLE)
    house_number = models.CharField(max_length=100, verbose_name='Номер дома', **NULLABLE)
    creation_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['email']


class Product(models.Model):
    """ Класс модели продукта """

    title = models.CharField(max_length=200, verbose_name='Название продукта')
    product_model = models.CharField(max_length=100, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода', **NULLABLE)
    price = models.FloatField(verbose_name='Цена', **NULLABLE)
    creation_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title']


class Company(models.Model):
    """ Класс модели компании """

    company_name = models.CharField(max_length=200, verbose_name='Название')
    types_sellers = models.IntegerField(choices=types_sellers, verbose_name='Тип сети', default=0)
    level = models.PositiveIntegerField(verbose_name='Уровень поставки')
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE, verbose_name='Контакты')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    supplier = models.ForeignKey('Company', on_delete=models.SET_NULL, verbose_name='Поставщик', **NULLABLE)
    debt = models.FloatField(verbose_name='Задолженность', **NULLABLE)
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    creation_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Пользователь')

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ['company_name']
