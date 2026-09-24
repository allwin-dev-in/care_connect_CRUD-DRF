from django import views
from rest_framework.views import APIView
from staff.models import Doctor
from rest_framework.response import Response

# Create your views here.

class DoctorsListCreateView(APIView):
    def get(self,request):
        qs=Doctor.objects.all().values()
        doctors_list=list(qs)
        return Response(data=doctors_list)

    def post(self,request):
        form_data=request.data
        Doctor.objects.create(**form_data)
        return Response(data={"message":"Record Created ..."})

class DoctorRetriveUpdateDeleteView(APIView):
    def get(self,request,pk=None):
        qs=Doctor.objects.filter(id=pk).values()
        return Response(data=qs)
    def put(self,request,pk=None):
        form_data=request.data
        Doctor.objects.filter(id=pk).update(**form_data)
        return Response({"message":"Recorded updated ..."})
    def delete(self,request,pk=None):
        Doctor.objects.filter(id=pk).delete()
        return Response({"message":"Record Deleted ..."})