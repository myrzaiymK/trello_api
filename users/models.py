from django.db import models
from django.contrib.auth.models import AbstractUser, Group


# Create your models here.
class CustomUser(AbstractUser):
    email_token = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)


