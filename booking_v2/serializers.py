
from rest_framework import serializers

from django.contrib.auth.models import User

from bookings.models import Appointment

from datetime import datetime

class SignupSerializer(serializers.ModelSerializer):
    class Meta:

        model=User
        fields=["username","email","password"]

class AppiontmentSeralizer(serializers.ModelSerializer):
    doctor=serializers.StringRelatedField() 

    class Meta:
        model=Appointment
        fields="__all__"
        read_only_fields=["id","token_number","appointment_time","created_at"]

    def validate(self,validated_data):
        valid_date= validated_data.get("appointment_date")
        doctor_id=validated_data.get("doctor")
        cust_phone=validated_data.get("phone")

        last_appoinment_object=Appointment.objects.filter(doctor=doctor_id,appointment_date=valid_date).last()
        appointment_date_objects=Appointment.objects.filter(doctor=doctor_id,appointment_date=valid_date)
        
        for i in appointment_date_objects:
            if cust_phone in i.phone:
                raise serializers.ValidationError("Appoiment with same phone already exists")
        if last_appoinment_object:
            if last_appoinment_object.token_number==2:
                raise serializers.ValidationError("Token is full on current date")
        if valid_date < datetime.today().date():
            raise serializers.ValidationError("Invalid Date, Appointment date cannot be in the past.")
        else:
            return validated_data

        