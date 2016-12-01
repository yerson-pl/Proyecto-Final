from rest_framework import viewsets
from americas_service_apps.evento.models.inasistencia import Inasistencia
from ..serializers.inasistencia import InasistenciaSerializer


class InasistenciaViewSet(viewsets.ModelViewSet):
    queryset = Inasistencia.objects.all()
    serializer_class = InasistenciaSerializer
