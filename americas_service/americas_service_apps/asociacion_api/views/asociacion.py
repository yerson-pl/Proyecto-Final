from rest_framework import viewsets
# from rest_framework.response import Response
# from django.db.models import Q
# from operator import __or__ as OR
# from functools import reduce


from ..serializers.asociacion import AsociacionSerializer
from americas_service_apps.asociacion.models.asociacion import Asociacion


# class AsociacionViewSet(viewsets.ModelViewSet):
#     queryset = Asociacion.objects.all()
#     serializer_class = AsociacionSerializer

#     def get_queryset(self):
#         query = self.request.query_params.get('query', '')
#         queryall = (Q(ruc__icontains=query),
#                     Q(nombre__icontains=query),
#                     Q(denominacion__icontains=query),
#                     Q(website__icontains=query),
#                     Q(logo__icontains=query)
#                     # Q(cuenta_banco__icontains=query)
#                     )
#         queryset = self.queryset.filter(reduce(OR, queryall))
#         return queryset

class AsociacionViewSet(viewsets.ModelViewSet):
    queryset = Asociacion.objects.all()
    serializer_class = AsociacionSerializer

    def get_queryset(self):
        try:
            cuenta_banco = self.request.GET.get('cuenta_banco')
            if cuenta_banco:
                queryset = Asociacion.objects.filter(
                    cuenta_banco__id=cuenta_banco)
            else:
                queryset = Asociacion.objects.all()
        except Exception as e:
            queryset = Asociacion.objects.all()

        return queryset
