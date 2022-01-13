from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ExcelFile
from .serializers import ExcelFileUploadSerializer, ExcelFileSerializer


class ExcelFileUploadView(APIView):
    parser_class = (FileUploadParser, )
    serializer_class = ExcelFileUploadSerializer

    def post(self, request, *args, **kwargs):
        excel_file = self.serializer_class(data=request.data)

        if not excel_file.is_valid():
            return Response(excel_file.errors, status=status.HTTP_400_BAD_REQUEST)

        excel_file.save()
        return Response(excel_file.data, status=status.HTTP_201_CREATED)


class ExcelFileDetailView(APIView):
    serializer_class = ExcelFileSerializer

    def get(self, request, pk):
        try:
            excel_file = ExcelFile.objects.get(pk=pk)
        except ExcelFile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(excel_file)

        return Response(serializer.data, status=status.HTTP_200_OK)
