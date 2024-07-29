from rest_framework import serializers
from api.main.models.role import Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = [
            'id', 'name', 'is_active', 'is_deleted', 'active_from', 'active_upto',
            'created_at', 'created_by', 'updated_at', 'updated_by', 'deleted_at', 'deleted_by'
        ]