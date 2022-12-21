from django.urls import path
from rest_framework import routers
from .views import TravelViewSet
urlpatterns = [
    path('travel/see',TravelViewSet.as_view({'get':'list'})),
    path('travel/create/',TravelViewSet.as_view({'post':'create'})),
    path('travel/update/<int:int>/',TravelViewSet.as_view({'put':'update'})),
    path('travel/delete/<int:int>/',TravelViewSet.as_view({'delete':'destroy'})),
]
