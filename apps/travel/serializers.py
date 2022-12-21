from rest_framework import serializers
from .models import Travel
class TravelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Travel
        fields = ('title','price','quantity''updated_at','description')