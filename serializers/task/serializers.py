from rest_framework.serializers import ModelSerializer

from task.models import Task, Category


class TaskModelSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'author', 'title', 'content', 'status', 'category', 'priority', 'created_date']


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_date']
