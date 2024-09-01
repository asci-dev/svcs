from django.urls import include
from django.urls import path
from rest_framework import routers
from .views import AddressViewSet

ver = 'v1'

router = routers.DefaultRouter()
router.register(f'api/{ver}/addresses', AddressViewSet)

urlpatterns = [
    path('', include(router.urls)),
]