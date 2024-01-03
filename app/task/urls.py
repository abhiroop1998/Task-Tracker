from django.urls import path
from .views import (
    TaskCreateview, TaskDetailView
)
urlpatterns = [
    path('', TaskCreateview.as_view(), name='task-create'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

]
