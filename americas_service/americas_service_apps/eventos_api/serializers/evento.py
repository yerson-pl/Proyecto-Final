from rest_framework import serializers
from americas_service_apps.evento.models.evento import Evento


class EventoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evento
        fields = '__all__'
