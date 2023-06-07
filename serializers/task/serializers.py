from rest_framework.serializers import ModelSerializer, ReadOnlyField

from task.models import Task, Category


class TaskModelSerializer(ModelSerializer):
    snippet = ReadOnlyField(source='get_snippet')

    class Meta:
        model = Task
        fields = ['id', 'author', 'title', 'content', 'snippet', 'status', 'category', 'priority', 'created_date']


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_date']
