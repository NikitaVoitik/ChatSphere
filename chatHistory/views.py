from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwner
from rest_framework.response import Response
from utils.exceptions import NO_PK_PROVIDED
from rest_framework import exceptions
from django.shortcuts import get_object_or_404

from .models import Chat
from .serializers import ChatSerializer


# Create your views here.

class ChatView(APIView):
    permission_classes = (IsAuthenticated, IsOwner)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is None:
            raise exceptions.ParseError(NO_PK_PROVIDED)

        chat = get_object_or_404(Chat, pk=pk)
        self.check_object_permissions(request, chat)
        serializer = ChatSerializer(chat)

        return Response(serializer.data, status=200)
