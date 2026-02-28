from django.core.management.base import BaseCommand
from apps.cuentas.models import Cuenta
from decimal import Decimal

class Command(BaseCommand):
    help = 'Resetea saldos para cuentas de usuarios para Load Test'

    def add_arguments(self, parser):
        parser.add_argument('--min', type=int, default=1)
        parser.add_argument('--max', type=int, default=1000)

    def handle(self, *args, **options):
        min_id = options['min']
        max_id = options['max']
        
        self.stdout.write(f'🔄 Reseteando saldos para cuentas entre ID {min_id} y {max_id}...')
        
        count = Cuenta.objects.filter(id__gte=min_id, id__lte=max_id).update(saldo=Decimal('1000000.00'))
        
        self.stdout.write(self.style.SUCCESS(f'✅ {count} cuentas actualizadas con saldo millonario.'))
        self.stdout.write('🚀 Seed completado.')
