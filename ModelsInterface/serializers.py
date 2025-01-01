from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Chat, ApiKey, ModelInterface

class ApiKeySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(allow_blank=True)
    model = serializers.PrimaryKeyRelatedField(queryset=ModelInterface.objects.all())
    api_key = serializers.CharField(write_only=True)

    class Meta:
        model = ApiKey
        fields = ('id', 'name', 'user', 'model', 'api_key')

    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        user = attrs.get('user')
        model = attrs.get('model')
        if ApiKey.objects.filter(user=user, model=model).exists():
            raise serializers.ValidationError("A key for this model already exists for this user")
        return attrs

    def create(self, validated_data):
        return ApiKey.objects.create(**validated_data)


class ModelInterfaceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()

    class Meta:
        model = ModelInterface
        fields = ('id', 'name', 'description')