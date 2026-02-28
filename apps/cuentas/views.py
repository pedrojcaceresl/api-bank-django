from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CuentaSerializer, TipoCuentaSerializer
from .services import (
    crear_cuenta, obtener_cuenta_por_id, obtener_cuentas, 
    obtener_cuentas_por_cliente, actualizar_saldo_cuenta,
    crear_tipo_cuenta, obtener_tipos_cuentas, obtener_tipo_cuenta_por_id
)

class CuentaListCreateView(APIView):
    def get(self, request):
        cliente_id = request.query_params.get('cliente_id')
        if cliente_id:
            cuentas = obtener_cuentas_por_cliente(cliente_id)
        else:
            cuentas = obtener_cuentas()
        serializer = CuentaSerializer(cuentas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CuentaSerializer(data=request.data)
        if serializer.is_valid():
            cuenta = crear_cuenta(serializer.validated_data)
            return Response(CuentaSerializer(cuenta).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CuentaDetailView(APIView):
    def get(self, request, id):
        cuenta = obtener_cuenta_por_id(id)
        if not cuenta:
            return Response({"error": "Cuenta no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CuentaSerializer(cuenta)
        return Response(serializer.data)

    def patch(self, request, id):
        nuevo_saldo = request.data.get('nuevoSaldo')
        if nuevo_saldo is None:
            return Response({"error": "El campo 'nuevoSaldo' es requerido"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            cuenta = actualizar_saldo_cuenta(id, nuevo_saldo)
            return Response(CuentaSerializer(cuenta).data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Tipo Cuenta Views
class TipoCuentaListCreateView(APIView):
    def get(self, request):
        tipos = obtener_tipos_cuentas()
        serializer = TipoCuentaSerializer(tipos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TipoCuentaSerializer(data=request.data)
        if serializer.is_valid():
            tipo = crear_tipo_cuenta(serializer.validated_data)
            return Response(TipoCuentaSerializer(tipo).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TipoCuentaDetailView(APIView):
    def get(self, request, id):
        tipo = obtener_tipo_cuenta_por_id(id)
        if not tipo:
            return Response({"error": "Tipo de cuenta no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TipoCuentaSerializer(tipo)
        return Response(serializer.data)
