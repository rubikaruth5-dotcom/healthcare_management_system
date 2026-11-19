from rest_framework import serializers


class AnalyticsSerializer(serializers.Serializer):

    total_patients = serializers.IntegerField()

    total_doctors = serializers.IntegerField()

    total_departments = serializers.IntegerField()

    total_appointments = serializers.IntegerField()

    completed_appointments = serializers.IntegerField()

    cancelled_appointments = serializers.IntegerField()