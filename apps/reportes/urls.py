from django.urls import path
from .views import ReporteTransaccionesView

urlpatterns = [
    path('transacciones/', ReporteTransaccionesView.as_view(), name='reporte-transacciones'),
]
