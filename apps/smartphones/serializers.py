from rest_framework import serializers
from .models import Brand, Smartphone, SmartImage


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "title slug".split()


class SmartImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartImage
        fields = 'image',


class SmartphoneListSerializer(serializers.ModelSerializer):
    smart_images = SmartImageSerializer(many=True)

    class Meta:
        model = Smartphone
        fields = "title price color slug smart_images".split()


class SmartphoneSerializer(serializers.ModelSerializer):
    smart_images = SmartImageSerializer(many=True)

    class Meta:
        model = Smartphone
        fields = ('title', 'slug', 'image', 'price', 'color', 'memory', 'quantity', 'in_stock', 'brand',
                  'description', 'created_at', 'updated_at', 'smart_images')


class SmartCreateSerializer(serializers.ModelSerializer):
    carousel_img = serializers.ListField(
        child=serializers.FileField(),
        write_only=True
    )

    class Meta:
        model = Smartphone
        fields = ('title', 'slug', 'image', 'price', 'color', 'memory', 'quantity', 'in_stock', 'brand',
                  'description', 'created_at', 'updated_at', 'carousel_img')

    def create(self, validated_data):
        carousel_images = validated_data.pop('carousel_img')
        smart = Smartphone.objects.create(**validated_data)
        images = []
        for image in carousel_images:
            images.append(SmartImage(smart=smart, image=image))
        SmartImage.objects.bulk_create(images)
        return smart

