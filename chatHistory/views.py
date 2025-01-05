import cuid
from django.shortcuts import get_object_or_404
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone

from users.permissions import IsOwner
from utils.default_chat_data import generate_default_chat_data
from utils.exceptions import NO_PK_PROVIDED
from .models import Chat
from .serializers import ChatSerializer, ChatMessagesSerializer


class ChatCreateView(APIView):
    permission_classes = (IsAuthenticated, IsOwner)

    def post(self, request, *args, **kwargs):
        chat = ChatSerializer(
            data=generate_default_chat_data(),
            context={'request': request}
        )

        chat.is_valid(raise_exception=True)
        chat.save()

        return Response(chat.data, status=201)

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

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is None:
            raise exceptions.ParseError(NO_PK_PROVIDED)

        chat = get_object_or_404(Chat, pk=pk)
        self.check_object_permissions(request, chat)

        for message in request.data.get('messages', []):
            message['id'] = cuid.cuid()
            message['timestamp'] = timezone.now()

        chat_serializer = ChatMessagesSerializer(chat, data=request.data, context={"action": "append"})
        chat_serializer.is_valid(raise_exception=True)
        chat_serializer.save()

        return Response(chat_serializer.data, 201)

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is None:
            raise exceptions.ParseError(NO_PK_PROVIDED)

        chat = get_object_or_404(Chat, pk=pk)
        self.check_object_permissions(request, chat)

        for message in request.data.get('messages', []):
            message['timestamp'] = timezone.now()

        chat_serializer = ChatMessagesSerializer(chat, data=request.data, context={"action": "edit"})
        chat_serializer.is_valid(raise_exception=True)
        chat_serializer.save()

        return Response(chat_serializer.data, 200)



