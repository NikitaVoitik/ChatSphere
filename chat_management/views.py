from django.forms.models import model_to_dict
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import ApiKey, ModelInterface
from .serializers import ApiKeySerializer, ModelInterfaceSerializer

class ApiKeyView(APIView):
    permission_classes = (IsAuthenticated,)


class ModelInterfaceView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            model_interfaces = ModelInterface.objects.all()
            serializer = ModelInterfaceSerializer(model_interfaces, many=True)

            return Response(serializer.data, status=200)
        else:
            model_interface = get_object_or_404(ModelInterface, pk=pk)
            serializer = ModelInterfaceSerializer(model_interface)

            return Response(serializer.data, status=200)




