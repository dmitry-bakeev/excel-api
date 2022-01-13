from rest_framework import serializers

from .models import ExcelFile


class ExcelFileUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExcelFile
        fields = (
            'id',
            'path',
        )
