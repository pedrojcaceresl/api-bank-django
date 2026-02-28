from django.db import models
from apps.cuentas.models import Cuenta

class Transaccion(models.Model):
    id = models.BigAutoField(primary_key=True)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='transacciones')
    tipo = models.CharField(max_length=30) # debito / credito
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'transacciones'

    def __str__(self):
        return f"Transaccion {self.id}: {self.tipo} - {self.monto}"
