from rest_framework import serializers
from api.main.models.user_role import UserRole

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = [
            'user', 'role', 'assigned_at'
        ]