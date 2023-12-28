from rest_framework import serializers

from app.core.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()