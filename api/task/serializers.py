from rest_framework.serializers import ModelSerializer
from .models import Task, AssignDetails  

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'priority',
            'tags', 'lead_time', 'deadline', 'approval_request',
            'assign_details', 'created', 'updated'
        ]
        
class AssignDetailsSerializer(ModelSerializer):
    class Meta:
        feilds = [
            'id', 'assignee', 'assignor', 'status',
            'status_update'
        ]