from rest_framework import serializers
from .models import Transaccion

class TransaccionSerializer(serializers.ModelSerializer):
    cuenta_id = serializers.IntegerField()

    class Meta:
        model = Transaccion
        fields = ['id', 'cuenta_id', 'tipo', 'monto', 'fecha']
        read_only_fields = ['id', 'fecha']
