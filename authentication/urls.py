from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
     #login for every user
     path('login',CustomTokenObtainPairView.as_view(), name="login"),
     #logout for every user
     path('api/logout/', LogoutView.as_view(), name="Logout"),
     #registration for admin
     path('registration/admin/', AdminRegistrationView.as_view(),
          name='register-admin'),
     # register a teacher user
     path('registration/teacher/', TeacherRegistrationView.as_view(),
          name='register-teacher'),
     # register a student
     path('registration/student/', StudentRegistrationView.as_view(),
          name='register-student'),
     path('api/passwordreset', PasswordReset.as_view(), name='Password reset confirm'),
     path('liststudents', StudentsList.as_view(), name="Student List"),
     path('listteachers', TeacherList.as_view(), name="Teacher List"),
]
