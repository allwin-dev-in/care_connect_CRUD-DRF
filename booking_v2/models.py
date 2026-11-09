import os

from dotenv import load_dotenv

from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail

from staff.models import Doctor

load_dotenv()

# Create your models here.

class Appointment(models.Model):

    patient_name = models.CharField(max_length=200)

    phone = models.CharField(max_length=15)

    email =models.EmailField(null=False)

    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name="Doctor")
    
    appointment_date = models.DateField()

    token_number = models.PositiveIntegerField(
        editable=False,
        null=True
    )

    appointment_time = models.TimeField(
        editable=False,
        null=True
    )

    problem = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return  self.patient_name

def send_email_token(sender,instance,created,*args,**kwargs):

    if created:
        send_mail(
            "Appointment Confirmation .",
            f""" Dear {instance.patient_name}, \n\t\t
            This is the mail for confirming your recent Doctor Booking. below is the Booking details,\n
            Appointment Date: {instance.appointment_date},\n
            Appointment Time: {instance.appointment_time},\n
            Patient Name : {instance.patient_name}\n
            Token Number : {instance.token_number}\n\n
            Thank you...""",
            {os.getenv("EMAIL_HOST_USER")},
            [instance.email]
        )
post_save.connect(send_email_token,sender=Appointment)