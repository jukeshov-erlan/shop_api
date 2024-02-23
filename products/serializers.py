from rest_framework import serializers
from .models import Category, Product, ProductImage


class ProductSerializer(serializers.ModelSerializer):
    in_stock = serializers.BooleanField(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = ProductImageSerializer(instance.images.all(), many=True).data
        return representation



class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'image', 'price', 'category']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class ProductImageSerializer(serializers.ModelSerializer):
    product = serializers.CharField(write_only=True)
    class Meta:
        model = ProductImage
        fields = 'product', 'image'
        # fields = '__all__'



