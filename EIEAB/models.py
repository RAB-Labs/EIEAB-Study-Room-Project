from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models






class UserProfile(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True, default='None')

    name = models.CharField(max_length=255, unique=False, default='None')
    idNumber = models.CharField(max_length=8, unique=False, default='None')


