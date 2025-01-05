from datetime import datetime
from rest_framework import serializers

from .models import Chat


class ContentSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=['text', 'image'])
    text = serializers.CharField(max_length=1024, required=False)
    image_url = serializers.URLField(required=False)

    def validate(self, data):
        if data['type'] == 'text' and not data.get('text'):
            raise serializers.ValidationError("Text content is required for type 'text'")
        if data['type'] == 'image' and not data.get('image_url'):
            raise serializers.ValidationError("Image URL is required for type 'image'")
        return data

class MessageSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    role = serializers.ChoiceField(choices=['user', 'assistant', 'developer'])
    content = ContentSerializer(many=True)
    timestamp = serializers.DateTimeField()

class ChatSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(allow_blank=True)
    messages = MessageSerializer(many=True)

    class Meta:
        model = Chat
        fields = ('user', 'name', 'messages')

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        #convert timestamp field to string, since in internal_value it has timestamp type
        for message in validated_data['messages']:
            if isinstance(message['timestamp'], datetime):
                message['timestamp'] = message['timestamp'].isoformat()
        return Chat.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass


