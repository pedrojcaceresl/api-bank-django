from django.urls import path
from .views import CuentaListCreateView, CuentaDetailView, CuentaSaldoView

urlpatterns = [
    path('', CuentaListCreateView.as_view(), name='cuenta-list'),
    path('<int:id>/', CuentaDetailView.as_view(), name='cuenta-detail'),
    path('<int:id>/saldo', CuentaSaldoView.as_view(), name='cuenta-saldo-no-slash'),
    path('<int:id>/saldo/', CuentaSaldoView.as_view(), name='cuenta-saldo'),
]
