from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet
from . import views

router = DefaultRouter()
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cars/', views.car_list, name='car_list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
