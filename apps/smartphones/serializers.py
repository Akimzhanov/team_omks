from rest_framework import serializers
from .models import Brand, Smartphone, SmartImage


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class SmartImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartImage
        fields = 'image',


class SmartphoneListSerializer(serializers.ModelSerializer):
    # smart_images = SmartImageSerializer(many=True)

    class Meta:
        model = Smartphone
        fields = "title price color image in_stock".split()


class SmartphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Smartphone
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['carousel'] = SmartImageSerializer(
            instance.smart_images.all(), many=True).data

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

