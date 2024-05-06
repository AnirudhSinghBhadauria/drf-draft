from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from .models import Task, AssignDetails
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import (
    TaskSerializer, AssignDetailsSerializer
)

class TaskViewSet(ViewSet):
    def list(self, request: Request):
        queryset = Task.objects.all()
        serializer = TaskSerializer(instance=queryset, many=True)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def retrieve(self, request: Request, pk=None):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(instance=task)
        
        return Response(
            data= serializer.data,
            status=status.HTTP_200_OK
        )
        
    def create(self, request: Request, pk=None):
        serializer = TaskSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(
                data = serializer.data,
                status = status.HTTP_201_CREATED
            )
        else:
            return Response(
                data={
                    "message": "Error while crating a new task!",
                    "error": serializer.errors,
                    "serializer_error": serializer.error_messages
                }
            )
    
    def update(self, request: Request, pk=None):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(
            task,
            data = request.data,
            partial = True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                data= serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data = {
                    "message": f"Updating task with id: {task.id} un-succesfull",
                    "error": serializer.errors,
                    "serializer_error": serializer.error_messages
                }
            )

    
    def delete(self, request, pk=None):
        task = Task.objects.get(pk=pk)
        
        task.delete()

        return Response(
            data = {
                "message": f"Task with id: {task.id} deleted succesfully!"
            }
        )

class AssignDetailsViewSet(ViewSet):
    def list(self, request: Request):
        queryset = AssignDetails.objects.all()
        serializer = AssignDetailsSerializer(
            instance=queryset, many=True
        )

        return Response(
            data= serializer.data,
            status=status.HTTP_200_OK
        )

    def retrieve(self, request: Request, pk=None):
        assign_details = get_object_or_404(AssignDetails, pk=pk)
        serializer = AssignDetailsSerializer(instance=assign_details)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
    
    def create(self, request: Request, pk=None):
        serializer = AssignDetailsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                data = serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data={
                    "message": "Assinging details creation failed",
                    "error": serializer.errors,
                    "serializer_error": serializer.error_messages
                }
            )
        
    def update(self, request: Request, pk=None):
        assign_details = AssignDetails.objects.get(pk=pk)
        serializer = AssignDetailsSerializer(
            assign_details,
            data=request.data,
            partial = True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                data=serializer.data,
                status=status.HTTP_202_ACCEPTED
            )
        else:
            return Response(
                data={
                    "message": "Assing details update un-succesfull",
                    "error": serializer.errors,
                    "serializer_errors": serializer.error_messages
                }
            )

    def delete(self, request: Request, pk=None):
        assign_detials = AssignDetails.objects.get(pk=pk)
        
        assign_detials.delete()
        
        return Response(
            data={
                "message": f"Assign details with id: {assign_detials.id}deleted succesfully!"
            },
            status=status.HTTP_200_OK
        )