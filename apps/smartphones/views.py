from django.shortcuts import render
from .models import Brand, Smartphone
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .serializers import (BrandSerializer, SmartphoneListSerializer, SmartphoneSerializer)
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import (ListAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView,
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
    serializer_class = SmartphoneSerializer
    # permission_classes = [IsAdminUser]


class SmartphoneUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer
    # permission_classes = [IsAdminUser]
    lookup_field = 'slug'

    # def get_permissions(self):
    #     if self.action in ['create', 'destroy', 'update', 'partial_update']:
    #         self.permission_classes = [IsAdminUser]
    #     if self.action in ['list', 'retrieve']:
    #         self.permission_classes = [AllowAny]


class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandAPIView(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'slug'



