from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny
from apps.smartphones.models import Smartphone
from apps.smartphones.serializers import SmartSerializer, SmartListSerializer

class SmartView(ModelViewSet):
    queryset = Smartphone.objects.all()
    serializer_class = SmartSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return SmartListSerializer
        elif self.action == 'create':
            return SmartSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdminUser]
        elif self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

