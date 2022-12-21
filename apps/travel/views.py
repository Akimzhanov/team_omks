from rest_framework import viewsets
from .models import Travel
from .serializers import TravelSerializer
class TravelViewSet(viewsets.ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer


