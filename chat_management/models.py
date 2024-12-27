from django.db import models
from django.contrib.auth.models import User
from common.models import TimeStampedModel

class ModelInterface(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.name + ' - ' + self.url + ' - ' + self.description

class ApiKey(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=1000)
    model = models.ForeignKey(ModelInterface, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username + ' - ' + self.model.name

class Chat(TimeStampedModel):
    api_key = models.ForeignKey(ApiKey, on_delete=models.CASCADE)
    chat = models.JSONField()

    def __str__(self):
        return self.api_key.user.username + ' - ' + self.api_key.model.name
