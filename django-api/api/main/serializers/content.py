from rest_framework import serializers
from api.main.models.content import Content

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = [
            'module', 'module_field', 'assigned_at'
        ]