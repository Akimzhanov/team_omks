from rest_framework.routers import DefaultRouter

from .views import OrderViewSet, OrderTravelViewSet

router = DefaultRouter()
router.register('order', OrderViewSet, 'orders')
router.register('ordertravel',OrderTravelViewSet, 'ordertravels')

urlpatterns = [

]

urlpatterns += router.urls

