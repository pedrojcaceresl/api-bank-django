from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClienteSerializer
from .services import crear_cliente, obtener_clientes, obtener_cliente_por_id

class ClienteListCreateView(APIView):
    def get(self, request):
        clientes = obtener_clientes()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            cliente = crear_cliente(serializer.validated_data)
            return Response(ClienteSerializer(cliente).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClienteDetailView(APIView):
    def get(self, request, id):
        cliente = obtener_cliente_por_id(id)
        if not cliente:
            return Response({"error": "Cliente no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)
