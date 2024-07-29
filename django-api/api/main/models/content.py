from django.db import models
from django.conf import settings
from api.main.models.module import Module
from api.main.models.module_field import ModuleField
class Content(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    module_field = models.ForeignKey(ModuleField, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'content'

    def __str__(self):
        return f'{self.module.name} - {self.module_field.table}'