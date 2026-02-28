from django.db import models
from apps.cuentas.models import Cuenta

class Transferencia(models.Model):
    id = models.BigAutoField(primary_key=True)
    cuenta_origen = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='transferencias_origen')
    cuenta_destino = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='transferencias_destino')
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'transferencias'

    def __str__(self):
        return f"Transferencia {self.id}: {self.cuenta_origen.id} -> {self.cuenta_destino.id} (${self.monto})"
