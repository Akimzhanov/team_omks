from django.urls import path
from . import views

urlpatterns = [
    path('', views.SmartphoneListAPIView.as_view()),
    path('create/', views.SmartphoneCreateAPIView.as_view()),
    path('<slug:slug>/', views.SmartphoneAPIView.as_view()),
    path('<slug:slug>/update/', views.SmartphoneUpdateAPIView.as_view()),

    path('brands/', views.BrandListAPIView.as_view()),
    path('brands/<slug:slug>', views.BrandAPIView.as_view())
]
