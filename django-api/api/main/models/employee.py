from django.db import models
from django.conf import settings
from api.main.models.gender import Gender

class Employee(models.Model):
    code = models.CharField(db_index=True, max_length=55, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=55)
    middle_name = models.CharField(max_length=55, blank=True, null=True)
    last_name = models.CharField(max_length=55)
    date_of_birth = models.DateField()
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    phone_no = models.CharField(max_length=15, unique=True, blank=True, null=True)
    date_of_joining = models.DateField()
    date_of_releaving = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    active_from = models.DateField(null=True, blank=True)
    active_upto = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='employees_created', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='employees_updated', null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='employees_deleted', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.code})"