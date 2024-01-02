from django.urls import path
from .views import (
    TaskCreateview
)
urlpatterns = [
    path('', TaskCreateview.as_view(), name='task-create'),
]
