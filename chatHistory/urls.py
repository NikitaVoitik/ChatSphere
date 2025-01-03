from django.urls import path
from .views import ChatView

urlpatterns = [
    path("chat/", ChatView.as_view(), name="model_list"),
    path("chat/<int:pk>/", ChatView.as_view(), name="model"),
]