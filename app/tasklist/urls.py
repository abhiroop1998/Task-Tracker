from django.urls import path
from .views import *

urlpatterns = [
    path('', TasklistCreateApiView.as_view(), name='tasklist-create'),
]
