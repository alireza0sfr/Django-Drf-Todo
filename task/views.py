from rest_framework.viewsets import ModelViewSet

from serializers.task.serializers import TaskModelSerializer, CategoryModelSerializer
from task.models import Task, Category


class TaskModelViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = TaskModelSerializer
    queryset = Task.objects.all()


class CategoryViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()
