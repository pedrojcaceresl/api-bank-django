from django.urls import path
from .views import TipoCuentaListCreateView, TipoCuentaDetailView

urlpatterns = [
    path('', TipoCuentaListCreateView.as_view(), name='tipos-cuentas-list'),
    path('<int:id>/', TipoCuentaDetailView.as_view(), name='tipos-cuentas-detail'),
]
