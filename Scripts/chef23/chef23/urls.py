from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib import admin

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('api.urls', namespace='api')),
    path('cook/', include('cook.urls', namespace='cook')),
    path('admin/', admin.site.urls),
] 