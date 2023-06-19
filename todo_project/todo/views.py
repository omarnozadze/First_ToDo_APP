
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render ,redirect
from rest_framework import status
from django.http import Http404

class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class Delete_task(APIView):
    def get_object(self, id):
        try:
            return Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            raise Http404

    def delete(self, request, id):
        todo = self.get_object(id)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
