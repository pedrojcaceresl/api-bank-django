from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TransaccionSerializer
from .services import obtener_transacciones, crear_batch_transacciones

class TransaccionListView(APIView):
    def get(self, request):
        desde = request.query_params.get('desde')
        hasta = request.query_params.get('hasta')
        cuenta_id = request.query_params.get('cuenta_id')
        limit = int(request.query_params.get('limit', 100))
        offset = int(request.query_params.get('offset', 0))

        # Max limit/offset as in controller
        if limit > 1000: limit = 1000
        if offset > 100000:
            return Response({"error": "Offset demasiado grande. Máximo permitido 100000"}, status=status.HTTP_400_BAD_REQUEST)

        transacciones = obtener_transacciones(desde, hasta, cuenta_id, limit, offset)
        serializer = TransaccionSerializer(transacciones, many=True)
        return Response(serializer.data)

class TransaccionBatchView(APIView):
    def post(self, request):
        transacciones_data = request.data.get('transacciones')
        if not isinstance(transacciones_data, list):
            return Response({"error": "El campo 'transacciones' debe ser un array"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            result = crear_batch_transacciones(transacciones_data)
            return Response(result, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TransaccionCuentaView(APIView):
    def get(self, request, id):
        limit = int(request.query_params.get('limit', 100))
        offset = int(request.query_params.get('offset', 0))
        
        transacciones = obtener_transacciones(cuenta_id=id, limit=limit, offset=offset)
        serializer = TransaccionSerializer(transacciones, many=True)
        return Response(serializer.data)
