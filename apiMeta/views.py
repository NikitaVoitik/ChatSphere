from django.forms.models import model_to_dict
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import exceptions

from utils.exceptions import NO_PK_PROVIDED
from users.permissions import IsOwnerOrPostOnly, IsOwner
from .models import ApiKey, ModelMeta
from .serializers import ApiKeySerializer, ModelInterfaceSerializer


class ApiKeyView(APIView):
    permission_classes = (IsAuthenticated, IsOwner)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            api_keys = ApiKey.objects.filter(user=request.user)
            serializer = ApiKeySerializer(api_keys, many=True)

            return Response(serializer.data, status=200)
        else:
            api_key = get_object_or_404(ApiKey, pk=pk)
            self.check_object_permissions(request, api_key)
            serializer = ApiKeySerializer(api_key)

            return Response(serializer.data, status=200)

    def post(self, request, *args, **kwargs):
        serializer = ApiKeySerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            raise exceptions.ParseError(NO_PK_PROVIDED)

        api_key = get_object_or_404(ApiKey, pk=pk)
        api_key.delete()

        return Response({'message': 'Api key deleted successfully'}, status=200)


class ModelInterfaceView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            model_interfaces = ModelMeta.objects.all()
            serializer = ModelInterfaceSerializer(model_interfaces, many=True)

            return Response(serializer.data, status=200)
        else:
            model_interface = get_object_or_404(ModelMeta, pk=pk)
            serializer = ModelInterfaceSerializer(model_interface)

            return Response(serializer.data, status=200)
