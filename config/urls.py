from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health', views.health_check),
    path('healthz', views.health_check),
    
    # API Routes v1
    path('api/v1/clientes/', include('apps.clientes.urls')),
    path('api/v1/cuentas/', include('apps.cuentas.urls')),
    path('api/v1/tipos-cuentas/', include('apps.cuentas.tipo_cuenta_urls')), # Separate route file for types
    path('api/v1/transacciones/', include('apps.transacciones.urls')),
    path('api/v1/transferencias/', include('apps.transferencias.urls')),
    path('api/v1/reportes/', include('apps.reportes.urls')),
    path('api/v1/setup/', include('apps.setup.urls')),
    
    # Extra Routes
    path('api/v1/health-check', views.health_check),
    path('api/v1/mensaje', views.mensaje),
    path('api/v1/saludar', views.saludar),

    # documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
