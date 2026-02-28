from .models import Cliente

def crear_cliente(data):
    return Cliente.objects.create(**data)

def obtener_clientes():
    return Cliente.objects.all()

def obtener_cliente_por_id(id):
    try:
        return Cliente.objects.get(id=id)
    except Cliente.DoesNotExist:
        return None
