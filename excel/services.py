from openpyxl import load_workbook

from django.utils import timezone

from .models import ExcelFile


def _get_columns_before_and_after(sheet):
    required = {'before', 'after'}
    need_len = 2
    result = {}

    first_row = sheet[1]

    if len(first_row) <= 1:
        return {}

    for i, cell in enumerate(first_row, start=1):
        if not cell.value:
            break

        if not required:
            break

        if cell.value in required:
            result.update({cell.value: i})
            required.remove(cell.value)

    if len(result.keys()) != need_len:
        return {}

    result.update({'sheet': sheet})

    return result


def _get_processing_result(required_columns):
    row_min = 2
    sheet = required_columns['sheet']

    before_column = required_columns['before']
    after_column = required_columns['after']

    before_list = list(
        next(sheet.iter_cols(min_col=before_column, max_col=before_column, min_row=row_min, values_only=True))
    )

    after_list = list(
        next(sheet.iter_cols(min_col=after_column, max_col=after_column, min_row=row_min, values_only=True))
    )

    result = ''

    if not before_list[-1]:
        result = 'added: '
        before_list.pop()

    if not after_list[-1]:
        result = 'removed: '
        after_list.pop()

    first_set = set()
    second_set = set()
    if len(before_list) > len(after_list):
        first_set = set(before_list)
        second_set = set(after_list)
    else:
        first_set = set(after_list)
        second_set = set(before_list)

    for item in first_set:
        if item not in second_set:
            return result + str(item)


def processing_excel_file(excel_file):
    work_book = load_workbook(excel_file.path)

    excel_file.processing_status = ExcelFile.ProcessingStatus.PROCESSING
    excel_file.save(update_fields=['processing_status', ])

    required_columns = None
    for sheet in work_book.worksheets:
        tmp = _get_columns_before_and_after(sheet)
        if tmp:
            required_columns = tmp
            break
    result = _get_processing_result(required_columns)

    excel_file.processing_result = result
    excel_file.processing_status = ExcelFile.ProcessingStatus.PROCESSED
    excel_file.processing_stop = timezone.now()
    excel_file.save(
        update_fields=[
            'processing_result', 'processing_status', 'processing_stop'
        ]
    )
