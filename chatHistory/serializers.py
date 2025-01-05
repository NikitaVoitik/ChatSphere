from datetime import datetime
from rest_framework import serializers

from .models import Chat


class ContentSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=['text', 'image'])
    text = serializers.CharField(max_length=1024, required=False)
    image_url = serializers.URLField(required=False)

    def validate(self, attrs):
        attrs = super().validate(attrs)

        if attrs['type'] == 'text' and not attrs.get('text'):
            raise serializers.ValidationError({"type": "Text content is required for type 'text'"})
        if attrs['type'] == 'image' and not attrs.get('image_url'):
            raise serializers.ValidationError({"type": "Image URL is required for type 'image'"})
        return attrs


class MessageSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    role = serializers.ChoiceField(choices=['user', 'assistant', 'developer'])
    content = ContentSerializer(many=True)
    timestamp = serializers.DateTimeField()

    def to_internal_value(self, data):
        if isinstance(data['timestamp'], datetime):
            data['timestamp'] = data['timestamp'].isoformat()

        return data


class ChatSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(allow_blank=True, required=False)
    messages = MessageSerializer(many=True, required=False)

    class Meta:
        model = Chat
        fields = ('id', 'user', 'name', 'messages')

    def create(self, validated_data):
        if self.context.get('request'):
            validated_data['user'] = self.context.get('request').user

        return Chat.objects.create(**validated_data)


class ChatMessagesSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)

    class Meta:
        model = Chat
        fields = ('messages',)

    def update(self, instance, validated_data):
        action = self.context.get('action')
        messages = validated_data.get('messages', [])

        if action == 'edit':
            message_ids = [m.get('id') for m in messages]
            earliest_index = 0
            for i, message in enumerate(instance.messages):
                if message.get('id') in message_ids:
                    earliest_index = i
                    break

            if earliest_index is not None:
                instance.messages = [m for i, m in enumerate(instance.messages) if i < earliest_index]

        instance.messages.extend(messages)
        instance.save()

        return instance
