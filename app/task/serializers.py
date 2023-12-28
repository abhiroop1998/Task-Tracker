from rest_framework import serializers

from app.core.models import Task


class TaskSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
