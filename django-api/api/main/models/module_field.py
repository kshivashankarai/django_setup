from django.db import models
from django.conf import settings
from api.main.models.module import Module

class ModuleField(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='metadata')
    table = models.CharField(max_length=255)
    column = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    active_from = models.DateField(null=True, blank=True)
    active_upto = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='modulefields_created', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='modulefields_updated', null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='modulefields_deleted', null=True, blank=True)
    
    def __str__(self):
        return f"{self.table}.{self.column} ({self.module.name})"