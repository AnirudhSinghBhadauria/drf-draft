from rest_framework.viewsets import ViewSet, ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import PostSerializer
from rest_framework import  status
from .models import Post

class PostViewSet(ViewSet):
    def list(self, request: Request):
        queryset = Post.objects.all()
        serializer = PostSerializer(instance = queryset, many = True)

        return Response(data=serializer.data, status = status.HTTP_200_OK)
    
    def retrieve(self, request: Request, pk = None):
        post = get_object_or_404(Post, pk = pk)
        serializer = PostSerializer(instance = post)

        return Response(data = serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request: Request):
        serializer = PostSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status = status.HTTP_201_CREATED)
        else:
            return  Response(
                data = {
                    "message": "Request unsuccesful, CREATING_USER", 
                    "error": serializer.errors, 
                    "ser_error": serializer.error_messages
                }
            )
            
    def update(self, request: Request, pk = None):
        post = Post.objects.get(pk = pk)
        serializer = PostSerializer(post, data= request.data)

        if serializer.is_valid(): 
            serializer.save()
            return Response(data = serializer.data, status=status.HTTP_200_OK)
        
        return Response(
            data = {
                    "message": "Request unsuccesful, UPDATING_USER", 
                    "error": serializer.errors, 
                    "ser_error": serializer.error_messages
                },
            status= status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
    def delete(self, request: Request, pk = None):
        post = Post.objects.get(pk = pk)
        post.delete()

        return Response(
            data = {
                "message": "Deleted post succesfully done",
            }, 
            status= status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
        
