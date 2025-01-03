from rest_framework import serializers
from .models import Chat
from django.contrib.auth.models import User


class ChatSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(allow_blank=True)
    chat = serializers.JSONField()

    class Meta:
        model = Chat
        fields = ('user', 'name', 'chat')
