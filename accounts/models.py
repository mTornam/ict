from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Staff(AbstractUser):
    phone_number = models.CharField(max_length=10, blank=False)
    other_names = models.CharField(max_length=255, blank=True)
    force_password_change = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.username