from django.urls import path
from .views import (
    TasklistCreateApiView
)

urlpatterns = [
    path('', TasklistCreateApiView.as_view(), name='tasklist-create'),
]
