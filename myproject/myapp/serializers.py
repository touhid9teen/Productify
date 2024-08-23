from rest_framework import serializers
from .models import Product


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'



class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.FloatField()
    stock = serializers.IntegerField()
    price_with_tax = serializers.SerializerMethodField(method_name="Calculate")

    def Calculate(self, product):
        return product.price * 1.18
        
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    