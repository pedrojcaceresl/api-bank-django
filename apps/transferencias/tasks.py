from celery import shared_task
from .services import crear_transferencia
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True, max_retries=3, default_retry_delay=1)
def task_realizar_transferencia(self, cuenta_origen_id, cuenta_destino_id, monto):
    try:
        transferencia = crear_transferencia(cuenta_origen_id, cuenta_destino_id, monto)
        return {"status": "completed", "transfer_id": transferencia.id}
    except Exception as exc:
        # Business errors (insufficient balance, etc.) should not be retried infinitely if they are logical
        # But we follow the original logic where it might throw and BullMQ retries based on attempts
        if "Saldo insuficiente" in str(exc) or "no encontrada" in str(exc):
            logger.error(f"Error de negocio en transferencia: {str(exc)}")
            raise exc
        
        # Retry for transient errors (DB locks, etc.)
        logger.warning(f"Error transitorio, reintentando: {str(exc)}")
        raise self.retry(exc=exc)
