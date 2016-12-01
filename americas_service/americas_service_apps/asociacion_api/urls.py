from django.conf.urls import url, include
from rest_framework import routers

from .views.asociacion import AsociacionViewSet
from .views.banco import CuentaBancoViewSet

router = routers.DefaultRouter()

router.register(r'asociacion', AsociacionViewSet)
router.register(r'banco', CuentaBancoViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
