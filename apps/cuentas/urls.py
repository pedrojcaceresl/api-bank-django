from django.urls import path
from .views import CuentaListCreateView, CuentaDetailView

urlpatterns = [
    path('', CuentaListCreateView.as_view(), name='cuenta-list'),
    path('<int:id>/', CuentaDetailView.as_view(), name='cuenta-detail'),
]
