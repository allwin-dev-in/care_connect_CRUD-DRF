from rest_framework import serializers

from datetime import datetime

class AppointmentSerializer(serializers.Serializer):
    patient_name = serializers.CharField()
    phone=serializers.CharField()
    doctor=serializers.IntegerField()
    appointment_date=serializers.DateField()
    token_number=serializers.IntegerField(read_only=True)
    appointment_time=serializers.TimeField(read_only=True)
    problem=serializers.CharField()
    created_at=serializers.DateTimeField(read_only=True)

    def validate(self, validated_data):

        self.appointment_date=validated_data.get("appointment_date")

        if self.appointment_date < datetime.today().date():
            raise serializers.ValidationError("invalid date")
        else:
            return validated_data


        

