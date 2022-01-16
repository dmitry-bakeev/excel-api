from django.db import transaction
from django.db.models import signals
from django.dispatch import receiver

from .models import ExcelFile
from .tasks import start_processing_excel


@receiver(signals.post_save, sender=ExcelFile)
def start_processing(instance, created, **kwargs):
    if not created:
        return

    transaction.on_commit(lambda: start_processing_excel.delay(instance.pk))
