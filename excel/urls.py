from django.urls import path

from . import views


urlpatterns = [
    path('upload/', views.ExcelFileUploadView.as_view()),
]
