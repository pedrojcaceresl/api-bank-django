from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TransferenciaSerializer
from .services import crear_transferencia, obtener_transferencia_por_id
from .tasks import task_realizar_transferencia

class TransferenciaCreateView(APIView):
    def post(self, request):
        cuenta_origen_id = request.data.get('cuenta_origen_id')
        cuenta_destino_id = request.data.get('cuenta_destino_id')
        monto = request.data.get('monto')

        if not all([cuenta_origen_id, cuenta_destino_id, monto]):
            return Response({"error": "Faltan campos requeridos"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            transferencia = crear_transferencia(cuenta_origen_id, cuenta_destino_id, monto)
            serializer = TransferenciaSerializer(transferencia)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            error_msg = str(e)
            if "Saldo insuficiente" in error_msg:
                return Response({"error": "Saldo insuficiente"}, status=status.HTTP_409_CONFLICT)
            if "no encontrada" in error_msg:
                return Response({"error": error_msg}, status=status.HTTP_404_NOT_FOUND)
            # Handle lock/serialization errors
            if "deadlock" in error_msg.lower() or "serialization" in error_msg.lower():
                return Response({"error": "Conflicto de concurrencia, por favor reintente"}, status=status.HTTP_409_CONFLICT)
            
            return Response({"error": "Error interno"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TransferenciaAsyncView(APIView):
    def post(self, request):
        cuenta_origen_id = request.data.get('cuenta_origen_id')
        cuenta_destino_id = request.data.get('cuenta_destino_id')
        monto = request.data.get('monto')

        if not all([cuenta_origen_id, cuenta_destino_id, monto]):
            return Response({"error": "Faltan campos requeridos"}, status=status.HTTP_400_BAD_REQUEST)

        # Enqueue task
        job = task_realizar_transferencia.delay(cuenta_origen_id, cuenta_destino_id, monto)

        return Response({
            "message": "Transferencia en proceso",
            "jobId": job.id,
            "status": "queued"
        }, status=status.HTTP_202_ACCEPTED)

class TransferenciaDetailView(APIView):
    def get(self, request, id):
        transferencia = obtener_transferencia_por_id(id)
        if not transferencia:
            return Response({"error": "Transferencia no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TransferenciaSerializer(transferencia)
        return Response(serializer.data)
