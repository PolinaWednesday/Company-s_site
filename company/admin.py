from django.contrib import admin
from rest_framework.exceptions import ValidationError
from .models import Contacts, Product, Company
from .serializers.company import CompanyCreateSerializers


@admin.action(description='Очистить задолженность')
def set_null_debt(ModelAdmin, request, queryset):
    """ Действие, очищающее задолженность (меняет поле debt=0) """
    queryset.update(debt=0)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    """ Админка контактов """
    list_display = ('id', 'email', 'country', 'city', 'street', 'house_number', 'creation_owner')
    list_filter = ('country', 'city')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Админка продуктов """
    list_display = ('id', 'title', 'product_model', 'release_date', 'price', 'creation_owner')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """ Админка Компании """
    list_display = ('id', 'company_name', 'types_sellers', 'level', 'contact', 'product', 'supplier', 'debt',
                    'creation_time', 'creation_owner')
    list_filter = ('contact__city', 'contact__country')
    actions = [set_null_debt]

    def save_model(self, request, obj, form, change):
        serializer = CompanyCreateSerializers(data=request.POST)
        if serializer.is_valid():
            obj.save()
        else:
            raise ValidationError('Ошибка согласованности полей. Проверьте поля "Уровень поставки", '
                                  '"Тип сети" и "Поставщик"')
