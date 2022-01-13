from django.urls import path

from . import views


urlpatterns = [
    path('upload/', views.ExcelFileUploadView.as_view()),
    path('detail/<int:pk>/', views.ExcelFileDetailView.as_view()),
]
