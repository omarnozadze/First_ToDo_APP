from . import views
from django.urls import include, path

urlpatterns = [
    path('todos/', views.TodoList.as_view()),
    path('todos/<int:pk>/', views.TodoDetail.as_view()),
    path('todos/<int:id>/delete/', views.Delete_task.as_view(), name='todo_delete'),
    
    ]