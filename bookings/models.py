from django.db import models

from staff.models import Doctor

# Create your models here.

from django.db import models

class Appointment(models.Model):

    patient_name = models.CharField(max_length=200)

    phone = models.CharField(max_length=15)

    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    
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