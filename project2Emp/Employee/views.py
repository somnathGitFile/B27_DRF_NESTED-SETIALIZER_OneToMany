from django.shortcuts import render
from .models import Employee, Project
from Employee.serializers import EmployeeSeializer, ProjectSerializer
from rest_framework import generics
# Create your views here.

class Employeedetails(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSeializer

class EmployeeInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSeializer

class ProjectDetails(generics.ListCreateAPIView):
    queruset= Project.objects.all()
    serializer = ProjectSerializer
