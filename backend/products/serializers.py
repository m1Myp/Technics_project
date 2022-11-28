from rest_framework import serializers

from .models import Categories, Info


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['category_name']


class Product_serializer(serializers.ModelSerializer):
    product_category_ID = CategorySerializer()

    class Meta:
        model = Info
        fields = ['product_name', 'product_category_ID', 'product_manufacturer']
