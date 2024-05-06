from rest_framework.serializers import ModelSerializer
from .models import User, Authorization
from django.contrib.auth.hashers import make_password
        
class AuthorizationSerializer(ModelSerializer):
    class Meta:
        model = Authorization
        fields = [
            'id', 'user_email', 'administrator',
            'status', 'status_update'
        ]
    
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'email', 'password', 'first_name',
            'last_name', 'role', 'authorization',
            'created', 'updated'
        ]
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)