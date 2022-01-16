from main.celery import app

from .models import ExcelFile
from .services import processing_excel_file


@app.task
def start_processing_excel(excel_file_pk):
    excel_file = ExcelFile.objects.get(pk=excel_file_pk)
    processing_excel_file(excel_file)
