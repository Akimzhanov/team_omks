from rest_framework import serializers
from .models import Smartphone, SmartImage


class SmartImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartImage
        fields = 'image',


class SmartListSerializer(serializers.ModelSerializer):
    smart_images = SmartImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Smartphone
        fields = "title slug price color in_stock smart_images".split()


class SmartSerializer(serializers.ModelSerializer):
    smart_images = SmartImagesSerializer(many=True, read_only = True)
    carousel_img = serializers.ListField(
        child=serializers.FileField(),
        write_only=True
    )

    class Meta:
        model = Smartphone
        fields = '__all__'

    def create(self, validated_data):
        carousel_images = validated_data.pop('carousel_img')
        smart = Smartphone.objects.create(**validated_data)
        images = []
        for image in carousel_images:
            images.append(SmartImage(smart=smart, image=image))
        SmartImage.objects.bulk_create(images)
        return smart

   