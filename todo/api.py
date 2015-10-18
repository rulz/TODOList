# encoding: utf-8
from django.contrib.auth.models import User

from rest_framework import serializers, viewsets, mixins, permissions
from rest_framework.decorators import detail_route, list_route

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope

from .models import Task


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Uso HyperlinkedModelSerializer para crear el serializador automáticamente
    con los campos del modelo, además para la relación con otro modelo se refleje 
    mediante una url
    """

    class Meta:
        model = User
        fields = ('url', 'pk', 'username', 'email', 'is_staff', 'password')
        extra_kwargs = {
            'url': {'view_name': 'users-detail', 'lookup_field': 'pk'},
        }


class UserViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    CRU del modelo User
    """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    paginate_by = 10
    paginate_by_param = 'page_size'
    max_paginate_by = 100

    #encriptar la clave
    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(str(user.password))
        user.save()

    def perform_update(self, serializer):
        user = serializer.save()
        user.set_password(str(user.password))
        user.save()


#********MYModel******
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    """
    Uso HyperlinkedModelSerializer para crear el serializador automáticamente
    con los campos del modelo, además para la relación con otro modelo se refleje 
    mediante una url
    """
    done = serializers.BooleanField(required=False)

    class Meta:
        model = Task
        fields = ('url', 'pk', 'assigned_to', 'name',
                  'description', 'done', 'created', 'modified')
        extra_kwargs = {
            'url': {'view_name': 'tasks-detail', 'lookup_field': 'pk'},
            'assigned_to': {'view_name': 'users-detail', 'lookup_field': 'pk'}
        }


class TaskViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """
    CRUD del modelo Task
    """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    paginate_by = 10
    paginate_by_param = 'page_size'
    max_paginate_by = 100
