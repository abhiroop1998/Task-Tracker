from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from app.utils import get_response_schema, get_global_error_messages, get_global_success_messages
from app.user.serializers import UserSerializer, LoginSerializer

# Swagger imports
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Create your views here.
class UserCreateAPIView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            },
        )
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return get_response_schema({}, get_global_success_messages()['NEW_USER_CREATED'], status.HTTP_201_CREATED)
        return get_response_schema(serializer.errors, get_global_error_messages()['BAD_REQUEST'], status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            },
        )
    )
    def post(self, request):
        try:
            serializers = LoginSerializer(data=request.data)
            if serializers.is_valid():
                email = serializers.data['email']
                password = serializers.data['password']
                user = authenticate(email=email, password=password)

                if not user:
                    return get_response_schema({}, get_global_error_messages()['INVALID_CREDENTIALS'], status.HTTP_401_UNAUTHORIZED)
                else:
                    refresh = RefreshToken.for_user(user)

                    return_data = {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    }
                    return get_response_schema(return_data, get_global_success_messages()['LOGIN_SUCCESSFUL'], status.HTTP_200_OK)
            return get_response_schema(serializers.errors, get_global_error_messages()['BAD_REQUEST'], status.HTTP_400_BAD_REQUEST)
        except Exception as exception:
            return get_response_schema({}, get_global_error_messages()['SOMETHING_WENT_WRONG'], status.HTTP_500_INTERNAL_SERVER_ERROR)


class LogoutAPIView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'refresh': openapi.Schema(type=openapi.TYPE_STRING),
            },
        )
    )
    def post(self, request):
        try:
            refresh = request.data['refresh']
            print(refresh)
            token = RefreshToken(refresh)
            token.blacklist()

            return_data = {
                "message": "Logout successfully",
                "success": True
            }

            return get_response_schema(return_data, get_global_success_messages()['LOGOUT_SUCCESSFUL'], status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return get_response_schema(str(e), get_global_error_messages()['BAD_REQUEST'], status.HTTP_400_BAD_REQUEST)
