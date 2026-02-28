import random
import time
from apps.clientes.models import Cliente
from apps.cuentas.models import Cuenta, TipoCuenta
from decimal import Decimal

def crear_dataset(cantidad=10):
    # Crear tipos de cuenta básicos si no existen
    tipos_data = [
        {"nombre": "Ahorros", "descripcion": "Cuenta de ahorros"},
        {"nombre": "Corriente", "descripcion": "Cuenta corriente"}
    ]
    
    for t in tipos_data:
        TipoCuenta.objects.get_or_create(nombre=t["nombre"], defaults={"descripcion": t["descripcion"]})
    
    tipos_all = list(TipoCuenta.objects.all())
    
    created_clientes = []
    created_cuentas = []
    saldo_inicial = Decimal("1000.00")
    
    for i in range(cantidad):
        timestamp = int(time.time() * 1000)
        cliente = Cliente.objects.create(
            nombre=f"Cliente {timestamp}_{i}",
            email=f"cliente{timestamp}_{i}@test.local"
        )
        created_clientes.append(cliente)
        
        cuentas_por_cliente = random.randint(1, 3)
        for j in range(cuentas_por_cliente):
            tipo = tipos_all[(i + j) % len(tipos_all)]
            numero = f"{timestamp}{i}{j}"[:20]
            cuenta = Cuenta.objects.create(
                cliente=cliente,
                tipo_cuenta=tipo,
                numero_cuenta=numero,
                saldo=saldo_inicial
            )
            created_cuentas.append(cuenta)
            
    return {"clientes": created_clientes, "cuentas": created_cuentas}
