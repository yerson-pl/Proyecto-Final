from rest_framework import serializers
from americas_service_apps.evento.models.asistencia import Asistencia


class AsistenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asistencia
        fields = '__all__'
