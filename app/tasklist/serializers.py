from rest_framework import serializers

from app.core.models import TaskList, Task


class TaskListCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = ('pk', 'title', 'user')
        extra_kwargs = {'user': {'write_only': True}}

class TaskListDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = ('pk', 'title')

class TaskListDisplaySerialzers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('pk', 'title', 'description', 'due_date', 'priority', 'status',)