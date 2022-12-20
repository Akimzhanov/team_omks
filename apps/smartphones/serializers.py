from rest_framework import serializers
from .models import Brand, Smartphone


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "title slug".split()


class SmartphoneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Smartphone
        fields = "title price color slug".split()


class SmartphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Smartphone
        fields = ('title', 'slug', 'image', 'price', 'color', 'memory', 'quantity', 'in_stock', 'brand',
                  'description', 'created_at', 'updated_at', 'smart_images')

