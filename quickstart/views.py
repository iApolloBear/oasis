from django.shortcuts import render
from .serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import Group, User
from rest_framework import viewsets


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows user to be viewed or edited
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows group to be viewed or edited
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
