from django.db import models
from django.conf import settings
from api.main.models.content import Content
from api.main.models.permission import Permission
from api.main.models.role import Role
class RolePermission(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'role_permission'

    def __str__(self):
        return f'{self.module.name} - {self.module_field.table}'