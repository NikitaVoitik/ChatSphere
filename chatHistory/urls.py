from django.urls import path
from .views import ChatView, ChatCreateView

urlpatterns = [
    path("", ChatCreateView.as_view(), name="chat"),
    path("<int:pk>/", ChatView.as_view(), name="chat"),
]