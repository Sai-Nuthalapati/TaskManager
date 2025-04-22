from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from tasks.models import Task
from .serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskForkView(APIView):
    """
    Duplicates a task (like Unix `fork`).
    """
    def post(self, request, pk):
        original_task = get_object_or_404(Task, pk=pk)
        cloned_task = Task.objects.create(
            name=original_task.name + " (copy)",
            description=original_task.description,
            status=original_task.status,
        )
        serializer = TaskSerializer(cloned_task)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
