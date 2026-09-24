from django.db import models

# Create your models here.

# Doctor (name,specialization,fee,qualification,email)


class Doctor(models.Model):

    name = models.CharField(max_length=200)

    SPECIALIZATION_OPTIONS = (
        
        ("cardiology", "Cardiology"),
        ("dermatology", "Dermatology"),
        ("endocrinology", "Endocrinology"),
        ("ent", "Ear, Nose & Throat (ENT)"),
        ("gastroenterology", "Gastroenterology"),
        ("general_medicine", "General Medicine / Internal Medicine"),
        ("general_surgery", "General Surgery"),
        ("gynecology", "Gynecology & Obstetrics"),
        ("hematology", "Hematology"),
        ("nephrology", "Nephrology"),
        ("neurology", "Neurology"),
        ("oncology", "Oncology"),
        ("ophthalmology", "Ophthalmology"),
        ("orthopedics", "Orthopedics"),
        ("pediatrics", "Pediatrics"),
        ("psychiatry", "Psychiatry"),
        ("pulmonology", "Pulmonology"),
        ("radiology", "Radiology"),
        ("urology", "Urology"),
        ("other", "Other"),
    )


    specialization = models.CharField(max_length=200,choices=SPECIALIZATION_OPTIONS,default="other")

    fee = models.PositiveIntegerField()

    qualification = models.CharField(max_length=200)

    email = models.EmailField(unique=True)

    #string representaion of object 
    def __str__(self):

        return self.name