from dataclasses import fields
from .models import Employee, Project
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class EmployeeSeializer(serializers.ModelSerializer):
    emp_project = ProjectSerializer(read_only = True, many=True)
    class Meta:
        model = Employee
        fields = '__all__'