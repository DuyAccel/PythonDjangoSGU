from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=26, primary_key=True, verbose_name="username")
    email = models.EmailField(unique=True, null=False, verbose_name='email')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []