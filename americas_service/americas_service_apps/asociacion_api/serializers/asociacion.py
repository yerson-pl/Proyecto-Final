from rest_framework import serializers
from americas_service_apps.asociacion.models.asociacion import Asociacion
from americas_service_apps.asociacion.models.cuenta_banco import CuentaBanco


class AsociacionSerializer(serializers.ModelSerializer):
    cuenta_banco = serializers.SlugRelatedField(
        slug_field='entidad_bancaria', queryset=CuentaBanco.objects.all())

    class Meta:
        model = Asociacion
        fields = '__all__'
