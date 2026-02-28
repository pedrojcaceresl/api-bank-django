from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.transacciones.services import obtener_transacciones
from apps.transacciones.serializers import TransaccionSerializer

class ReporteTransaccionesView(APIView):
    def get(self, request):
        desde = request.query_params.get('desde')
        hasta = request.query_params.get('hasta')
        limit = int(request.query_params.get('limit', 1000))
        offset = int(request.query_params.get('offset', 0))

        transacciones = obtener_transacciones(desde, hasta, limit=limit, offset=offset)
        serializer = TransaccionSerializer(transacciones, many=True)
        return Response(serializer.data)
