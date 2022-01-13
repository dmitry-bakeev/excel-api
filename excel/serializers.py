from rest_framework import serializers

from .models import ExcelFile


class ExcelFileUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExcelFile
        fields = (
            'id',
            'path',
        )


class ExcelFileSerializer(serializers.ModelSerializer):

    processing_status = serializers.SerializerMethodField()

    def get_processing_status(self, obj):
        return obj.get_processing_status_display()

    class Meta:
        model = ExcelFile
        fields = (
            'id',
            'path',
            'processing_stop',
            'processing_status',
            'processing_result',
            'created_at',
        )
