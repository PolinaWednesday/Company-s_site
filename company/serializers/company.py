from rest_framework import serializers

from company.models import Company
from company.serializers.contacts import ContactsSerializers
from company.serializers.product import ProductSerializers
from company.validators import CompanyValidator


class CompanyCreateSerializers(serializers.ModelSerializer):
    """ Класс сериализатора для cоздания компании """

    level = serializers.IntegerField(required=False)

    class Meta:
        model = Company
        fields = ['name', 'types_sellers', 'level', 'contact', 'product', 'supplier', 'debt',
                  'creation_time']
        validators = [CompanyValidator()]

    def create(self, validated_data):
        """ Метод создания поставщика """
        request = self.context.get('request')
        if request and request.user:
            validated_data['creation_owner'] = request.user

        if validated_data.get('supplier'):
            supplier = validated_data['supplier']
            validated_data['level'] = supplier.level + 1
        elif validated_data.get('types_sellers') == 0:
            validated_data['level'] = 0

        return super().create(validated_data)


class CompanySerializers(serializers.ModelSerializer):
    """ Класс сериализатора компании """

    contact = ContactsSerializers(read_only=True)
    product = ProductSerializers(read_only=True)
    types_sellers = serializers.CharField(source='get_types_sellers_display')

    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ('debt', 'creation_time', 'creation_owner', )

    def validate(self, data):
        """ Метод валидации компании """
        print(data)
        request = self.context.get('request')
        if not request.user.is_superuser:
            if self.instance and any(field in data for field in ["level", "get_types_sellers_display", "supplier"]):
                raise serializers.ValidationError(
                    "Обновление данных полей запрещено. "
                    "Обратитесь к администратору сайта, если вам необходимо изменить данные.")

        return data
