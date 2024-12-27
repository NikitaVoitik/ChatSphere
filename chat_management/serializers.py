from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Chat, ApiKey, ModelInterface

class ApiKeySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    model = serializers.StringRelatedField()
    api_key = serializers.CharField()

    class Meta:
        model = ApiKey
        fields = ('id', 'user', 'model', 'api_key')

    def create(self, validated_data):
        return ApiKey.objects.create(**validated_data)


class ModelInterfaceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()

    class Meta:
        model = ModelInterface
        fields = ('id', 'name', 'description')