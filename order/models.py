from django.db import models
from user.models import CustomUser


# Create your models here.

class UserCard(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
