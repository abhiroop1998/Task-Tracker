from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from app.core.models import TaskList, Task
from app.core.views import CustomPageNumberPagination
from app.utils import get_response_schema, get_global_success_messages, get_global_error_messages
from app.tasklist.serializers import (
    TaskListCreateSerializers,
    TaskListDetailSerializers, TaskListDisplaySerialzers, TaskListFilterSerializers
)

# Swagger imports
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

import logging

logger = logging.getLogger(__name__)


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

        task = Task.objects.select_related('task_list').filter(task_list_id=pk, is_active=True, status=True)
        task_list = self.get_object(pk, request)
        if task_list and task:
            task_list_serializer = TaskListDetailSerializers(task_list)
            task_serializer = TaskListDisplaySerialzers(task, many=True)
            data = {
                **task_list_serializer.data,
                'task': task_serializer.data
            }
            return get_response_schema(data, get_global_success_messages()['RECORD_RETRIEVED'], status.HTTP_200_OK)
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
            task_queryset = Task.objects.filter(task_list_id=pk, status=True, is_active=True)
            if task_queryset:
                task_queryset.update(is_active=False)

            return get_response_schema({}, get_global_success_messages()['RECORD_DELETED'], status.HTTP_200_OK)
        return get_response_schema({}, get_global_error_messages()['BAD_REQUEST'], status.HTTP_404_NOT_FOUND)


class TaskListFilterView(ListAPIView):
    serializer_class = TaskListFilterSerializers
    pagination_class = CustomPageNumberPagination

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        task_list_queryset = TaskList.objects.filter(user_id=self.request.user.id, is_active=True)

        if self.request.GET.get('title'):
            task_list_queryset = task_list_queryset.filter(title__icontains=self.request.GET.get('title'))

        if not task_list_queryset:
            return []

        return task_list_queryset

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('title', openapi.IN_QUERY, type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
