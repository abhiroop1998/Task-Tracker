from rest_framework import serializers

from app.core.models import Task


class TaskSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('pk', 'title', 'description', 'due_date', 'priority', 'status', 'task_list')
