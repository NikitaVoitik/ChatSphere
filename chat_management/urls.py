from django.urls import path
from .views import ModelInterfaceView

urlpatterns = [
    path("model/", ModelInterfaceView.as_view(), name="model"),
    path("model/<int:pk>/", ModelInterfaceView.as_view(), name="model_get"),
]