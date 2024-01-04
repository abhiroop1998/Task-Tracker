from django.urls import path
from .views import (
    TaskCreateview, TaskDetailView, TaskListFilter
)
urlpatterns = [
    path('', TaskCreateview.as_view(), name='task-create'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('list-filter/', TaskListFilter.as_view(), name='task-list-filter'),

]
