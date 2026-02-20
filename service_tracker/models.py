from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class ServiceRecord(models.Model):
    class DeviceType(models.TextChoices):
        AIO = 'aio', 'AIO'
        LAPTOP = 'laptop', 'Laptop'
        SYSTEM_UNIT = 'system unit', 'System Unit'
        MONITOR = 'monitor', 'Monitor'
        OTHER = 'other', 'Other'

    class ProblemType(models.TextChoices):
        NETWORK = 'network', 'Network'
        SOFTWARE = 'software', 'Software'
        HARDWARE = 'hardware', 'Hardware'
        OTHER = 'other', 'Other'

    class District(models.TextChoices):
        ADENTA = 'adenta', 'Adenta'
        LEGON = 'legon', 'Legon'
        TESHIE = 'teshie', 'Teshie'
        MAKOL = 'makola', 'Makola'
        ROMAN_RIDGE = 'roman ridge', 'Roman Ridge'
        DODOWA = 'dodowa', 'Dodowa'
        MAMPONG = 'mampong', 'Mampong'
        KWABENYA = 'kwabenya', 'Kwabenya'
        REGIONAL_OFFICE = 'regional office', 'Regional office'    


    # requester
    requester_name = models.CharField(max_length=100)
    requester_contact = models.CharField(max_length=10)
    # device
    device_name = models.CharField(max_length=50)
    device_type = models.CharField(choices=DeviceType.choices, default=DeviceType.SYSTEM_UNIT, max_length=20)
    # problem
    problem_type = models.CharField(choices=ProblemType.choices , default=ProblemType.SOFTWARE, max_length=10)
    problem_desc = models.TextField(blank=True, null=True)
    # office
    district = models.CharField(choices=District.choices, default=District.REGIONAL_OFFICE, max_length=20)
    room_number= models.CharField(max_length=3, blank=True, null=True)
    # time tracking
    received_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(blank=True, null=True)
    # staff tracking
    received_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='received_jobs')
    # status
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.requester_name}: {self.device_name}"
    
    class Meta:
        ordering = ['-received_at']
   