from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
# Create your models here.
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=128, blank=True, null=True)
    avatar = models.ImageField(upload_to='Images/', blank=True, null=True)