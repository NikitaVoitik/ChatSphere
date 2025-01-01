from django.contrib import admin
from .models import ModelMeta, ApiKey

@admin.register(ModelMeta)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url')

@admin.register(ApiKey)
class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('user', 'api_key', 'model')
