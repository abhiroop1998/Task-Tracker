from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from app.utils import get_response_schema, get_global_success_messages, get_global_error_messages
from .serializers import TaskSerialzer
from ..core.models import TaskList, Task

# Swagger imports
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Create your views here.


class TaskCreateview(GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING),
                'description': openapi.Schema(type=openapi.TYPE_STRING),
                'due_date': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE),
                'priority': openapi.Schema(type=openapi.TYPE_STRING, enum=[Task.Priority.HIGH, Task.Priority.MEDIUM, Task.Priority.LOW]),
                'status': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                'task_list': openapi.Schema(type=openapi.TYPE_INTEGER),
            },
        )
    )
    def post(self, request):

        try:
            task_list = TaskList.objects.get(id=request.data['task_list'], user_id=request.user.id)
            request.data['task_list'] = task_list.id
            serializer = TaskSerialzer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return get_response_schema(serializer.data, get_global_success_messages()['RECORD_CREATED'],
                                           status.HTTP_201_CREATED)
            return get_response_schema(serializer.errors, get_global_error_messages()['SOMETHING_WENT_WRONG'],
                                       status.HTTP_400_BAD_REQUEST)
        except TaskList.DoesNotExist:
            return get_response_schema({}, get_global_error_messages()['BAD_REQUEST'], status.HTTP_404_NOT_FOUND)
