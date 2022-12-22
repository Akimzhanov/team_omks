from rest_framework import serializers
from apps.travel.models import TravelImages, Travel


class TravelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelImages
        fields = '__all__'

class TravelSerializer(serializers.ModelSerializer):
    picture = TravelImagesSerializer(many=True, read_only=True)
    class Meta:
        model = Travel
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        all_data = request.FILES
        travel = Travel.objects.create(**validated_data)

        TravelImages.objects.bulk_create(
            [TravelImages(travel=travel, picture=image) for image in all_data.getlist('picture')]
        )
        return travel

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        print(TravelSerializer(instance.travel_images.all(), many=True))
        rep['picture'] = TravelImagesSerializer(instance.travel_images.all(), many=True).data
        return rep