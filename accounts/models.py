from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	phone_number = models.CharField(max_length=13, blank=True, null=True, default='998901234567')
	avatar = models.ImageField(upload_to='media/', null=True)
	