from django.db import models
from django.contrib.auth.models import User
from common.models import TimeStampedModel

class ModelMeta(TimeStampedModel):
    name = models.CharField(max_length=100)
    request_name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    text_completions = models.BooleanField(null=False, default=False)
    image_generation = models.BooleanField(null=False, default=False)
    vision = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.name + ' - ' + self.url + ' - ' + self.description

class ApiKey(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    api_key = models.CharField(max_length=1000)
    model = models.ForeignKey(ModelMeta, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f"API Key {ApiKey.objects.filter(user=self.user).count() + 1}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username + ' - ' + self.model.name

    class Meta:
        unique_together = ['user', 'model']
