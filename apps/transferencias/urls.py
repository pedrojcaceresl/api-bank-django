from django.urls import path
from .views import TransferenciaCreateView, TransferenciaAsyncView, TransferenciaDetailView

urlpatterns = [
    path('', TransferenciaCreateView.as_view(), name='transferencia-create'),
    path('async/', TransferenciaAsyncView.as_view(), name='transferencia-async'),
    path('<int:id>/', TransferenciaDetailView.as_view(), name='transferencia-detail'),
]
