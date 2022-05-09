from django.shortcuts import render
from .models import Employee, Project
from demo.serializers import EmployeeSerializer, ProjectSerializer
from rest_framework import generics
# Create your views here.

class Employee_Info(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ProjectInfo(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
