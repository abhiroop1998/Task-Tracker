from django.urls import path
from .views import (
    TasklistCreateApiView, TaskListDetailApiView
)

urlpatterns = [
    path('', TasklistCreateApiView.as_view(), name='tasklist-create'),
    path('<int:pk>/', TaskListDetailApiView.as_view(), name='tasklist-detail'),
]
