from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.smartphones.views import SmartView

router = DefaultRouter()
router.register('', SmartView)

urlpatterns = [
    path('', include(router.urls))
]

