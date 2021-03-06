from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import serializers, viewsets
from rest_framework import permissions
from rest_framework import generics
from quickstart.serializers import (
    UserSerializer,
    GroupSerializer,
    UserSerializerHyperLink,
)

# Create your views here.
class UserReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializerHyperLink


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerHyperLink


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerHyperLink


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializerHyperLink
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]