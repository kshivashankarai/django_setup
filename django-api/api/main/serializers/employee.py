from rest_framework import serializers
from api.main.models.employee import Employee
from api.main.models.gender import Gender
from api.main.serializers.gender import GenderSerializer

class EmployeeSerializer(serializers.ModelSerializer):
     
    gender_name = serializers.SerializerMethodField()
    gender_id = serializers.IntegerField(source='gender.id', read_only=True)

    class Meta:
        model = Employee
        fields = [
            'code', 'email', 'first_name', 'middle_name', 'last_name',
            'date_of_birth', 'gender_id', 'gender_name', 'phone_no', 
            'date_of_joining', 'date_of_releaving', 'is_active', 
            'is_staff', 'is_deleted', 'active_from', 'active_upto', 
            'created_at', 'created_by', 'updated_at', 'updated_by', 
            'deleted_at', 'deleted_by'
        ]
    def get_gender_name(self, obj):
        return obj.gender.name if obj.gender else None
