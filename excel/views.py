from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.views import APIView

from .serializers import ExcelFileUploadSerializer


class ExcelFileUploadView(APIView):
    parser_class = (FileUploadParser, )
    serializer_class = ExcelFileUploadSerializer

    def post(self, request, *args, **kwargs):
        excel_file = self.serializer_class(data=request.data)

        if not excel_file.is_valid():
            return Response(excel_file.errors, status=HTTP_400_BAD_REQUEST)

        excel_file.save()
        return Response(excel_file.data, status=HTTP_201_CREATED)
