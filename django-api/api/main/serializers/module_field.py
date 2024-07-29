from rest_framework import serializers
from api.main.models.module_field import ModuleField

class ModuleFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleField
        fields = [
                'module', 'table', 'column', 'is_active', 'is_deleted', 
                'active_from', 'active_upto', 'created_at', 'created_by', 
                'updated_at', 'updated_by', 'deleted_at' 
            ]