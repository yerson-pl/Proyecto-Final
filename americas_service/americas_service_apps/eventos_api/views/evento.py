from rest_framework import viewsets
from americas_service_apps.evento.models.evento import Evento
from ..serializers.evento import EventoSerializer
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        queryall = (Q(id__icontains=query),
                    Q(nombre__icontains=query))
        queryset = self.queryset.filter(reduce(OR, queryall))
        return queryset
