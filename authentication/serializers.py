from django.db.models import fields
from rest_framework import serializers
from .models import *
from rest_framework.serializers import ModelSerializer
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
import os
from rest_framework.response import Response
import datetime
from distutils.dir_util import copy_tree
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
            # Custom data you want to include
            data.update({'user': self.user.username})
            data.update({'id': self.user.id})
            data.update({'email': self.user.email})
            data.update({'name':self.user.first_name+' '+self.user.last_name})
            data.update({'message':"login successful"})
            # and everything else you want to send in the response
            return data
        except:
            return {"message":"Login Failed"}
        
class AdminRegistrationSerializer(RegisterSerializer):
    admin = serializers.PrimaryKeyRelatedField(
        read_only=True,)  # by default allow_null = False

    def get_cleaned_data(self):
        data = super(AdminRegistrationSerializer, self).get_cleaned_data()
        return data

    def save(self, request):
        user = super(AdminRegistrationSerializer, self).save(request)
        user.is_admin = True
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.save()
        admin = Admin(admin=user)
        admin.save()
        return user


class TeacherRegistrationSerializer(RegisterSerializer):
    teacher = serializers.PrimaryKeyRelatedField(
        read_only=True,)  # by default allow_null = False
    mobile_no = serializers.IntegerField(required=False)
    description = serializers.CharField(required=False)

    def get_cleaned_data(self):
        data = super(TeacherRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            'description': self.validated_data.get('description', ''),
            'mobile_no': self.validated_data.get('mobile_no', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(TeacherRegistrationSerializer, self).save(request)
        user.is_teacher = True
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.save()
        teacher = Teacher(teacher=user)
        teacher.save()
        return user


class StudentRegistrationSerializer(RegisterSerializer):
    student = serializers.PrimaryKeyRelatedField(
        read_only=True,)  # by default allow_null = False

    def get_cleaned_data(self):
        data = super(StudentRegistrationSerializer, self).get_cleaned_data()
        return data

    def save(self, request):
        user = super(StudentRegistrationSerializer, self).save(request)
        user.is_student = True
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.save()
        student = Student(student=user)
        student.save()
        return user

