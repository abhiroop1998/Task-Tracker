from rest_framework import serializers

from app.core.models import TaskList


class TaskListCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = ('pk', 'title', 'user')
        extra_kwargs = {'user': {'write_only': True}}

