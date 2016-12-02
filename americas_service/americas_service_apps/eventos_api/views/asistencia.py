from rest_framework import viewsets
from americas_service_apps.evento.models.asistencia import Asistencia
from ..serializers.asistencia import AsistenciaSerializer
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce


class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', '')

        if query is not '':
	        queryall = (Q(socio_lote__socio__persona__documento_identidad__iexact=query),)
	        queryset = self.queryset.filter(reduce(OR, queryall))        
        	return queryset
        else:
        	return self.queryset