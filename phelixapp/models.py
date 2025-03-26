from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('worker', 'Worker'),
        ('employer', 'Employer'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='worker')

    # Fix the reverse accessor issue
    groups = models.ManyToManyField(Group, related_name="customuser_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_set", blank=True)
    
class WorkerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="worker_profile")
    full_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    skills = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class EmployerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="employer_profile")
    company_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
class Job(models.Model):
    employer = models.ForeignKey(EmployerProfile, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
