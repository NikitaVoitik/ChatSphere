from django.contrib import admin
from .models import Model, ApiKey, Chat

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url')

@admin.register(ApiKey)
class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('user', 'api_key', 'model')

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('api_key', 'chat')
