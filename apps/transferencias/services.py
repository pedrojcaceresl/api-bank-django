from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from apps.cuentas.models import Cuenta
from .models import Transferencia
from apps.transacciones.models import Transaccion
from decimal import Decimal

def crear_transferencia(cuenta_origen_id, cuenta_destino_id, monto):
    if not cuenta_origen_id or not cuenta_destino_id or monto is None:
        raise ValueError("Faltan datos requeridos para realizar la transferencia")

    monto_dec = Decimal(str(monto))
    origen_id = int(cuenta_origen_id)
    destino_id = int(cuenta_destino_id)

    with transaction.atomic():
        # DETERMINISTIC LOCK ORDER: lock lower ID first to prevent deadlocks
        first_lock_id = min(origen_id, destino_id)
        second_lock_id = max(origen_id, destino_id)

        # Lock both accounts
        # We need to use select_for_update()
        locks = Cuenta.objects.select_for_update().filter(id__in=[first_lock_id, second_lock_id])
        
        # Mapping locks back to origin/destination
        cuenta_origen = None
        cuenta_destino = None
        
        for acc in locks:
            if acc.id == origen_id:
                cuenta_origen = acc
            if acc.id == destino_id:
                cuenta_destino = acc

        if not cuenta_origen:
            raise ObjectDoesNotExist("Cuenta origen no encontrada")
        if not cuenta_destino:
            raise ObjectDoesNotExist("Cuenta destino no encontrada")

        if cuenta_origen.saldo < monto_dec:
            raise ValueError("Saldo insuficiente")

        # Update balances
        cuenta_origen.saldo -= monto_dec
        cuenta_origen.save()

        cuenta_destino.saldo += monto_dec
        cuenta_destino.save()

        # Create transfer record
        transferencia = Transferencia.objects.create(
            cuenta_origen=cuenta_origen,
            cuenta_destino=cuenta_destino,
            monto=monto_dec
        )

        # Create transaction records (debit/credit)
        Transaccion.objects.create(
            cuenta=cuenta_origen,
            tipo="debito",
            monto=monto_dec
        )
        Transaccion.objects.create(
            cuenta=cuenta_destino,
            tipo="credito",
            monto=monto_dec
        )

        return transferencia

def obtener_transferencia_por_id(id):
    try:
        return Transferencia.objects.get(id=id)
    except Transferencia.DoesNotExist:
        return None
