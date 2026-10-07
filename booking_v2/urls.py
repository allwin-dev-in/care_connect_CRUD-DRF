from django.urls import path

from booking_v2.views import SignupView
from booking_v2.views import AppointmentCreateListView
from booking_v2.views import AppointmentRetriveUpdateDeleteView

urlpatterns=[
    path("signup/",SignupView.as_view()),
    
    path("appointment/",AppointmentCreateListView.as_view()),
    path("appointment/<int:pk>/",AppointmentRetriveUpdateDeleteView.as_view()),
    
]