from .models import User
from rest_framework import permissions


class IsSuper(permissions.BasePermission):
    """
    Allows access only to "is_admin" users.
    """
    # def __init__(self, allowed_methods):
    #     super().__init__()
    #     self.allowed_methods = allowed_methods
    def has_permission(self, request, view):
        if request.user.is_admin:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_admin:
            return True
        return False


class IsStudent(permissions.BasePermission):
    """
    Allows access only to "is_student" users.
    """
    def has_permission(self, request, view):
        if request.user.is_student:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_student:
            return True
        return False


class IsTeacher(permissions.BasePermission):
    """
    Allows access only to "is_teacher" users.
    """

    def has_permission(self, request, view):
        if request.user.is_teacher:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_teacher:
            return True
        return False
