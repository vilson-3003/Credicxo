from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.serializers import Serializer
from .serializers import *
from rest_auth.registration.views import RegisterView
from .permission import *
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
import requests

# class LogoutView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request, *args, **kwargs):
#         print('here')
#         print(request.user.username)
#         User.objects.filter(
#             username=request.user.username).update(is_online=False)
#         # try:
#         #     query = Agentloginrecort.objects.filter(agent=request.user.username).last()
#         #     serializer = AgentLoginReportSerializer(query, data={'logout_datetime':str(datetime.datetime.now() + datetime.timedelta(seconds=0, minutes=30, hours=5)), 'sent':False})
#         #     if serializer.is_valid():
#         #         serializer.save()
#         # except:
#         #     pass
#         request.user.auth_token.delete()
#         logout(request)
#         # logger.info('[User] Logout - User {} with id {} logged out'.format(request.user.username, request.user.id))
#         return Response({"message": "success", 'code': status.HTTP_200_OK, 'detail': "logout success"})

class LogoutView(APIView):
    """
    Calls Django logout method and delete the Token object
    assigned to the current User object.
    Accepts/Returns nothing.
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        if getattr(settings, 'ACCOUNT_LOGOUT_ON_GET', False):
            response = self.logout(request)
        else:
            response = self.http_method_not_allowed(request, *args, **kwargs)

        return self.finalize_response(request, response, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.logout(request)

    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        if getattr(settings, 'REST_SESSION_LOGIN', True):
            logout(request)

        response = Response({"detail": ("Successfully logged out.")},
                            status=status.HTTP_200_OK)
        if getattr(settings, 'REST_USE_JWT', False):
            from rest_framework_jwt.settings import api_settings as jwt_settings
            if jwt_settings.JWT_AUTH_COOKIE:
                response.delete_cookie(jwt_settings.JWT_AUTH_COOKIE)
        return response


class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer

class TeacherRegistrationView(RegisterView):
    serializer_class = TeacherRegistrationSerializer


class StudentRegistrationView(RegisterView):
    serializer_class = StudentRegistrationSerializer


class AdminRegistrationView(RegisterView):
    serializer_class = AdminRegistrationSerializer

class PasswordReset(APIView):
    permission_classes = []

    def post(self, request, *agr, **kwargs):
        request.data['token'] = self.request.query_params.get('token')
        data = request.data
        url = "http://localhost:8000"+"/api/password_reset/confirm/"
        response = requests.post(url, json=data, timeout=10)
        return Response({"status": response})
#Showing Student list 
class StudentsList(APIView):
    permissions_class = (IsAuthenticated, IsSuper|IsTeacher)

    def get(self, request, *args, **kwargs):
        user = User.objects.filter(is_student=True)
        data = []
        for i in user:
            data.append({"name":i.first_name+" "+i.last_name, "username":i.username, "mobile":Student.objects.get(student=i.id).mobile_no})

        return Response({"all_students":data})

class TeacherList(APIView):
    permissions_class = [IsSuper]

    def get(self, request, *args, **kwargs):
        user = User.objects.filter(is_teacher=True)
        data = []
        for i in user:
            data.append({"name":i.first_name+" "+i.last_name, "username":i.username, "mobile":Teacher.objects.get(teacher=i.id).mobile_no})

        return Response({"all_teachers":data})