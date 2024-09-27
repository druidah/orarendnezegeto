from django.db import models
from django.contrib.auth.models import User
class Event(models.Model):
    summary = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.summary

class ICSLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Kapcsolat a felhasználóval, elvileg.
    url = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.url}"