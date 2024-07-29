from rest_framework import serializers
from api.main.models.role_permission import RolePermission

class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermission
        fields = [
            'content', 'permission', 'role', 'assigned_at' 
            ]