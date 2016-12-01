from rest_framework import serializers
from americas_service_apps.evento.models.inasistencia import Inasistencia


class InasistenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inasistencia
        fields = '__all__'
