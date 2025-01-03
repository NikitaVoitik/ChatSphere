from django.db import models
from common.models import TimeStampedModel
from django.contrib.auth.models import User

class Chat(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="New Chat")
    chat = models.JSONField()

    def __str__(self):
        return self.user.username + ' - ' + self.name

