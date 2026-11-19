from django.urls import path
from .views import (
    MedicalRecordListCreateView,
    MedicalRecordDetailView
)


urlpatterns = [

    path(
        'medical_records/',
        MedicalRecordListCreateView.as_view(),
        name='medical-record-list-create'
    ),

    path(
        '<int:pk>/',
        MedicalRecordDetailView.as_view(),
        name='medical-record-detail'
    ),
]