from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Staff(AbstractUser):
    phone_number = models.CharField(max_length=10, blank=False)

    # REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']
