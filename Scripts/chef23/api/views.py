from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from .serializers import UserSerializer


class isLoggedIn(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated == True:
            return True
        return False

def get_queryset():
    return User.objects.all().order_by('username')

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_queryset()
    serializer_class = UserSerializer
    permission_classes = [isLoggedIn]

# Create your views here.
