from rest_framework import viewsets
from americas_service_apps.evento.models.asistencia import Asistencia
from ..serializers.asistencia import AsistenciaSerializer


class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer
