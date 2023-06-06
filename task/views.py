from rest_framework.viewsets import ModelViewSet

from serializers.task.serializers import TaskModelSerializer, CategoryModelSerializer
from task.models import Task, Category
from enums.task import TaskStatus


class TaskModelViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = TaskModelSerializer
    queryset = Task.objects.filter(status=TaskStatus.PUBLISHED)
    # model = Task

    # def get_queryset(self):
    #     if self.action == 'list':
    #         return self.model.objects.filter(status=TaskStatus.PUBLISHED)
    #     elif self.action == 'retrieve':
    #         return self.model.objects.filter(id=self.kwargs['pk'])
    #     else:
    #         return super().get_queryset()



class CategoryViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()
