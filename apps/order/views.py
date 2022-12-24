from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Order, OrderTravel
from .serializers import OrderSerializer, OrderTravelSerializer

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)




class OrderTravelViewSet(ModelViewSet):
    serializer_class = OrderTravelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return OrderTravel.objects.filter(user=user)