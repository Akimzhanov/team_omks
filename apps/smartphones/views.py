from .models import Brand, Smartphone
from rest_framework.permissions import IsAdminUser, AllowAny
from .serializers import (BrandSerializer, SmartphoneListSerializer,
                          SmartphoneSerializer, SmartCreateSerializer)
from rest_framework.generics import (ListAPIView, ListCreateAPIView, CreateAPIView,
                                     RetrieveAPIView, RetrieveUpdateDestroyAPIView)


class SmartphoneListAPIView(ListAPIView):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneListSerializer
    permission_classes = [AllowAny]


class SmartphoneAPIView(RetrieveAPIView):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'


class SmartphoneCreateAPIView(CreateAPIView):
    queryset = Smartphone.objects.all()
    serializer_class = SmartCreateSerializer
    permission_classes = [IsAdminUser]


class SmartphoneUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Smartphone.objects.all()
    serializer_class = SmartCreateSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'


class BrandListAPIView(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer



