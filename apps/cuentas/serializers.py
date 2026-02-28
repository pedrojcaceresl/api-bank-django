from rest_framework import serializers
from .models import TipoCuenta, Cuenta

class TipoCuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCuenta
        fields = ['id', 'nombre', 'descripcion']

class CuentaSerializer(serializers.ModelSerializer):
    cliente_id = serializers.IntegerField(write_only=True)
    tipo_cuenta_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Cuenta
        fields = ['id', 'cliente_id', 'tipo_cuenta_id', 'numero_cuenta', 'saldo', 'created_at']
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        # Handle the IDs manually to match exact Prisma behavior if needed, 
        # but standard Django handle is fine.
        return Cuenta.objects.create(**validated_data)
