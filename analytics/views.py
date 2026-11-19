from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from django.db.models import Count, Q

from patients.models import Patient
from doctors.models import Doctor
from departments.models import Department
from appointments.models import Appointment

from .serializers import AnalyticsSerializer


class DashboardAnalyticsView(APIView):

    permission_classes = [IsAdminUser]

    def get(self, request):

        appointment_stats = Appointment.objects.aggregate(

            total=Count('id'),

            completed=Count(
                'id',
                filter=Q(status='Completed')
            ),

            cancelled=Count(
                'id',
                filter=Q(status='Cancelled')
            )
        )

        data = {
            'total_patients': Patient.objects.count(),

            'total_doctors': Doctor.objects.count(),

            'total_departments': Department.objects.count(),

            'total_appointments': appointment_stats['total'],

            'completed_appointments': appointment_stats['completed'],

            'cancelled_appointments': appointment_stats['cancelled'],
        }

        serializer = AnalyticsSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )