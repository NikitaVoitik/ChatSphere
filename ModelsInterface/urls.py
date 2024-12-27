from django.urls import path
from .views import ModelInterfaceView, ApiKeyView

urlpatterns = [
    path("model/", ModelInterfaceView.as_view(), name="model_list"),
    path("model/<int:pk>/", ModelInterfaceView.as_view(), name="model"),
    path("api-key/", ApiKeyView.as_view(), name="api_key_list"),
    path("api-key/<int:pk>/", ApiKeyView.as_view(), name="api_key"),
]