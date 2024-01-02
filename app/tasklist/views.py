from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from app.core.models import TaskList, Task
from app.utils import get_response_schema, get_global_success_messages, get_global_error_messages
from app.tasklist.serializers import (
    TaskListCreateSerializers,
    TaskListDetailSerializers
)

# Swagger imports
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Create your views here.


class TasklistCreateApiView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING)
            }
        )
    )
    def post(self, request):
        request.data['user'] = request.user.id
        serializer = TaskListCreateSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return get_response_schema(serializer.data, get_global_success_messages()['RECORD_CREATED'],
                                       status.HTTP_201_CREATED)
        return get_response_schema(serializer.errors, get_global_error_messages()['SOMETHING_WENT_WRONG'],
                                   status.HTTP_400_BAD_REQUEST)


class TaskListDetailApiView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self, pk, request):

        try:
            return TaskList.objects.get(id=pk, user_id=self.request.user.id, is_active=True)
        except TaskList.DoesNotExist:
            return None
    @swagger_auto_schema()
    def get(self, request, pk=None):

        task_list = self.get_object(pk, request)

        if task_list:
            serializer = TaskListDetailSerializers(task_list)
            return get_response_schema(serializer.data, get_global_success_messages()['RECORD_RETRIEVED'],
                                       status.HTTP_200_OK)
        return get_response_schema({}, get_global_error_messages()['BAD_REQUEST'], status.HTTP_404_NOT_FOUND)


    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING)
            }
        )
    )
    def patch(self, request, pk=None):

        task_list = self.get_object(pk, request)
        if task_list:
            serializer = TaskListDetailSerializers(task_list, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return get_response_schema(serializer.data, get_global_success_messages()['RECORD_UPDATED'],
                                           status.HTTP_200_OK)
            return get_response_schema(serializer.errors, get_global_error_messages()['SOMETHING_WENT_WRONG'],
                                       status.HTTP_400_BAD_REQUEST)
        return get_response_schema({}, get_global_error_messages()['BAD_REQUEST'], status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema()
    def delete(self, request, pk=None):

        task_list = self.get_object(pk, request)

        if task_list:
            task_list.is_active = False
            task_list.save()
            task_queryset = Task.objects.filter(task_list_id=pk)
            if task_queryset:
                task_queryset.update(is_active=False)

            return get_response_schema({}, get_global_success_messages()['RECORD_DELETED'], status.HTTP_200_OK)
        return get_response_schema({}, get_global_error_messages()['BAD_REQUEST'], status.HTTP_404_NOT_FOUND)