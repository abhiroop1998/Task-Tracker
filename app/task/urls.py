from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskCreateview.as_view(), name='task-create'),
]
