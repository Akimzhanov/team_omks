from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from apps.travel.models import Travel
from apps.travel.serializers import TravelSerializer




class TravelView(ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdminUser]
        elif self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]