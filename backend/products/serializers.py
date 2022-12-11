from rest_framework import serializers

from .models import Categories, Info, Pictures, Cost, URL


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ['category_name']


class PictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pictures
        fields = ['picture_URL']


class CostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cost
        fields = ['product_cost']


class URLSerializer(serializers.HyperlinkedModelSerializer):
    cost = CostSerializer()

    class Meta:
        model = URL
        fields = ['product_shop', 'product_URL', 'cost']


class Product_serializer(serializers.HyperlinkedModelSerializer):
    product_category_ID = CategorySerializer()
    pictures = PictureSerializer(many=True, read_only=True)
    urls = URLSerializer(many=True, read_only=True)

    class Meta:
        model = Info
        fields = ['product_ID', 'product_name', 'product_manufacturer', 'product_category_ID', 'pictures', 'urls']
