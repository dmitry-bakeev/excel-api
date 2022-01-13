import os

from hashlib import sha256
from pathlib import Path

from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.utils import timezone


def get_excel_file_path(excel_file, filename):
    now = timezone.now()
    filename_base, extension = os.path.splitext(filename)
    filename_base_hash = sha256(filename_base.encode()).hexdigest()
    filename_hash = filename_base_hash + extension
    return Path('excel') / str(now.year) / str(now.month) / str(now.day) / filename_hash


class ExcelFile(models.Model):

    class ProcessingStatus(models.IntegerChoices):
        LOADED = 0, 'Загружено'
        PROCESSING = 1, 'Обрабатывается'
        PROCESSED = 2, 'Обработано'

    path = models.FileField(
        upload_to=get_excel_file_path,
        validators=[FileExtensionValidator(allowed_extensions=('xls', 'xlsx'))],
        verbose_name='путь'
    )

    processing_stop = models.DateTimeField(null=True, blank=True, verbose_name='окончание обработки')
    processing_status = models.SmallIntegerField(
        choices=ProcessingStatus.choices,
        default=ProcessingStatus.LOADED,
        verbose_name='статус обработки'
    )
    processing_result = models.CharField(max_length=settings.LEN, blank=True, verbose_name='результат обработки')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'файл Excel'
        verbose_name_plural = 'файлы Excel'
        ordering = (
            'created_at',
        )
