from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	is_staff  = models.BooleanField(default=False)
	is_employee = models.BooleanField(default=False)
