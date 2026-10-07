from django.shortcuts import render
from django.contrib.auth.models import User


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView

from bookings.models import Appointment

from booking_v2.serializers import SignupSerializer
from booking_v2.serializers import AppiontmentSeralizer

from datetime import time,datetime,timedelta

# Create your views here.

class SignupView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=SignupSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            user_object=User.objects.create_user(**cleaned_data)
            ser_inst=SignupSerializer(user_object)
            return Response(data=ser_inst.data)
        else:
            return Response(serializer_instance.errors)

class AppointmentCreateListView(APIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):
        qs=Appointment.objects.all()
        serializer_instance=AppiontmentSeralizer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=AppiontmentSeralizer(data=form_data)

        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data

            #For doctorid,appointment_date
            doctor_id=cleaned_data.get("doctor")
            appointment_date=cleaned_data.get("appointment_date")

            #check for last appointment exists
            last_appointment_object=Appointment.objects.filter(doctor=doctor_id,appointment_date=appointment_date).last()

            appointment_time=time(10,0)
            if last_appointment_object:
                #tiken
                cleaned_data["token_number"]=last_appointment_object.token_number+1
                #time (if exist add 15 mins)
                next_appointment_date_time=datetime.combine(appointment_date,last_appointment_object.appointment_time)+timedelta(minutes=15)
                appointment_time=next_appointment_date_time.time()


            else:
                cleaned_data["token_number"]=1

            qs=Appointment.objects.create(**cleaned_data,appointment_time=appointment_time)
            ser_inst=AppiontmentSeralizer(qs)

            return Response(data=ser_inst.data)
        else:
            return Response(data=serializer_instance.errors)

class AppointmentRetriveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=AppiontmentSeralizer
    queryset=Appointment.objects.all()
            
