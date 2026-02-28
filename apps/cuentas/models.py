from django.db import models
from apps.clientes.models import Cliente

class TipoCuenta(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        db_table = 'tipos_cuenta'

    def __str__(self):
        return self.nombre

class Cuenta(models.Model):
    id = models.BigAutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cuentas')
    tipo_cuenta = models.ForeignKey(TipoCuenta, on_delete=models.CASCADE, related_name='cuentas')
    numero_cuenta = models.CharField(max_length=20)
    saldo = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cuentas'

    def __str__(self):
        return f"{self.numero_cuenta} - {self.cliente.nombre}"
