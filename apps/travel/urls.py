from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.travel.views import TravelView

router = DefaultRouter()
router.register('', TravelView)

urlpatterns = [
    path('api/', include(router.urls))
]