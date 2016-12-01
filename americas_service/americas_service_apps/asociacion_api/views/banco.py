from rest_framework import viewsets
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce

from ..serializers.banco import CuentaBancoSerializer
from americas_service_apps.asociacion.models.cuenta_banco import CuentaBanco


class CuentaBancoViewSet(viewsets.ModelViewSet):
    """
    Description: Model Description
    """
    queryset = CuentaBanco.objects.all()
    serializer_class = CuentaBancoSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        queryall = (Q(entidad_bancaria__icontains=query),
                    Q(tipo_cuenta__icontains=query),
                    Q(numero_cuenta__icontains=query))
        queryset = self.queryset.filter(reduce(OR, queryall))
        return queryset
