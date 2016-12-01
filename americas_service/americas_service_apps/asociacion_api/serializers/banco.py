from rest_framework import serializers
from americas_service_apps.asociacion.models.cuenta_banco import CuentaBanco


class CuentaBancoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CuentaBanco
        fields = '__all__'
