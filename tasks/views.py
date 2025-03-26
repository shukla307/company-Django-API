from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Task, User
from .serializers import TaskSerializer, UserSerializer

class TaskCreateView(generics.CreateAPIView):
    """Create a new task"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAssignView(generics.UpdateAPIView):
    """Assign task to users"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = self.get_serializer(task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class UserTasksView(generics.ListAPIView):
    """Get all tasks for a specific user"""
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Task.objects.filter(assigned_users__id=user_id)


# Create your views here.
