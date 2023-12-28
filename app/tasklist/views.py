
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from app.utils import get_response_schema, get_global_success_messages, get_global_error_messages
from app.tasklist.serializers import TaskListCreateSerializers

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
            return get_response_schema(serializer.data,get_global_success_messages()['RECORD_CREATED'], status.HTTP_201_CREATED)
        return get_response_schema(serializer.errors,get_global_error_messages()['SOMETHING_WENT_WRONG'], status.HTTP_400_BAD_REQUEST)