from rest_framework import serializers
from .models import Transferencia

class TransferenciaSerializer(serializers.ModelSerializer):
    cuenta_origen_id = serializers.IntegerField()
    cuenta_destino_id = serializers.IntegerField()

    class Meta:
        model = Transferencia
        fields = ['id', 'cuenta_origen_id', 'cuenta_destino_id', 'monto', 'fecha']
        read_only_fields = ['id', 'fecha']
