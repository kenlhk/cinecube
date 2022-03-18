import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    userID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=256)

    def __str__(self):
        return self.user.username
