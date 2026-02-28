from .models import Cuenta, TipoCuenta

# TipoCuenta services
def crear_tipo_cuenta(data):
    return TipoCuenta.objects.create(**data)

def obtener_tipos_cuentas():
    return TipoCuenta.objects.all()

def obtener_tipo_cuenta_por_id(id):
    try:
        return TipoCuenta.objects.get(id=id)
    except TipoCuenta.DoesNotExist:
        return None

# Cuenta services
def crear_cuenta(data):
    return Cuenta.objects.create(**data)

def obtener_cuenta_por_id(id):
    try:
        return Cuenta.objects.get(id=id)
    except Cuenta.DoesNotExist:
        return None

def obtener_cuentas():
    return Cuenta.objects.all()

def obtener_cuentas_por_cliente(cliente_id):
    return Cuenta.objects.filter(cliente_id=cliente_id)

def actualizar_saldo_cuenta(id, nuevo_saldo):
    cuenta = Cuenta.objects.get(id=id)
    cuenta.saldo = nuevo_saldo
    cuenta.save()
    return cuenta
