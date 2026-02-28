from django.urls import path
from .views import TransaccionListView, TransaccionBatchView, TransaccionCuentaView

urlpatterns = [
    path('', TransaccionListView.as_view(), name='transacciones-list'),
    path('batch/', TransaccionBatchView.as_view(), name='transacciones-batch'),
    path('cuenta/<int:id>/', TransaccionCuentaView.as_view(), name='transacciones-cuenta'),
]
