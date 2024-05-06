from rest_framework.viewsets import ViewSet, ModelViewSet
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, AuthorizationSerializer
from .models import User, Authorization
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(ViewSet):
    def list(slef, request: Request):
        queryset = User.objects.all()
        serializer = UserSerializer(
            instance=queryset, many=True
        )

        return Response(
            data = serializer.data, 
            status=status.HTTP_200_OK
        )
        
    def retrieve(self, request: Request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(instance=user)

        return Response(
            data = serializer.data, 
            status=status.HTTP_200_OK
        )
    
    def create(self, request: Request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(
                data=serializer.data, 
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data = {
                    "message": "Error while creating new user!",
                    "error": serializer.errors,
                    "serializer_error": serializer.error_messages
                }
            )
    
    def update(self, request: Request, pk=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(
            user,
            data = request.data,
            partial = True
        )
        
        if serializer.is_valid():
            serializer.save()

            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data = {
                    "message": f"Updating user with email {user.email} un-succesfull",
                    "error": serializer.errors,
                    "serializer_error": serializer.error_messages
                }
            )
    
    def delete(self, request: Request, pk=None):
        user = User.objects.get(pk=pk)

        user.delete()

        return Response(
            data={
                "message": f"User with email {user.email} deleted succesfully!",
            }
        )


class AuthorizationViewSet(ViewSet):
    def list(self, request: Request):
        queryset = Authorization.objects.all()
        serializer = AuthorizationSerializer(
            instance=queryset, many=True
        )

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
    
    def retrieve(self, request: Request, pk=None):
        authorization = get_object_or_404(Authorization, pk=pk)
        serializer = AuthorizationSerializer(instance=authorization)

        return Response(
            data=serializer.data, 
            status=status.HTTP_200_OK
        )

    
    def create(self, request: Request):
        serializer = AuthorizationSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                data=serializer.data, 
                status = status.HTTP_201_CREATED
            )
        else:
            return Response(
                data = {
                    "message": "Authorization creation failed",
                    "error": serializer.errors,
                    "serializer_error": serializer.error_messages
                }
            )
    
    def update(self, request: Request, pk = None):
        authorization = Authorization.objects.get(pk=pk)
        serializer = AuthorizationSerializer(
            authorization, 
            data = request.data,
            partial = True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                data= serializer.data,
                status= status.HTTP_200_OK
            )
        else:
            return Response(
                data={
                    "message": "Authorization update un-succesfull",
                    "error": serializer.errors,
                    "serializer_error": serializer.error_messages
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def delete(slef, request: Request, pk=None):
        authorization = Authorization.objects.get(pk=pk)

        authorization.delete()
        
        return Response(
            data={
                "message": 
                    f"Authorization for user with email: {authorization.user_email} deleted succesfully!",
            },
            status=status.HTTP_200_OK
        )
        
        
