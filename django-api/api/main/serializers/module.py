from rest_framework import serializers
from api.main.models.module import Module

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = [
                'code', 'name', 'table', 'description', 'is_active', 
                'is_deleted', 'active_from', 'active_upto', 'created_at', 
                'created_by', 'updated_at', 'updated_by', 'deleted_at', 
                'deleted_by'
            ]