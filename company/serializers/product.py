from rest_framework import serializers
from company.models import Product


class ProductSerializers(serializers.ModelSerializer):
    """ Класс сериализатора продукта """

    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'creation_owner': {'required': False}
        }

    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user:
            validated_data['creation_owner'] = request.user
        return super().create(validated_data)
