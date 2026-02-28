from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import crear_dataset

class SetupDatasetView(APIView):
    def post(self, request):
        cantidad = request.data.get('cantidad')
        if cantidad is None:
            return Response({"error": "El campo 'cantidad' (número de clientes) es requerido en el body"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            result = crear_dataset(int(cantidad))
            return Response({
                "ok": True,
                "summary": {
                    "clientes": len(result["clientes"]),
                    "cuentas": len(result["cuentas"])
                }
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
