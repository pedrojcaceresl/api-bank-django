from .models import Transaccion
from django.db.models import Q

def obtener_transacciones(desde=None, hasta=None, cuenta_id=None, limit=100, offset=0):
    queryset = Transaccion.objects.all().order_by('-fecha')
    
    if desde:
        queryset = queryset.filter(fecha__gte=desde)
    if hasta:
        queryset = queryset.filter(fecha__lte=hasta)
    if cuenta_id:
        queryset = queryset.filter(cuenta_id=cuenta_id)
        
    return queryset[offset:offset+limit]

def crear_batch_transacciones(transacciones_data):
    instances = [
        Transaccion(
            cuenta_id=t['cuenta_id'],
            tipo=t['tipo'],
            monto=t['monto']
        )
        for t in transacciones_data
    ]
    result = Transaccion.objects.bulk_create(instances)
    return {"count": len(result)}
