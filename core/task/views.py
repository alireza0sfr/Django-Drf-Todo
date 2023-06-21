from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from common.paginations import BasePagination
from serializers.task.serializers import TaskModelSerializer, CategoryModelSerializer
from task.models import Task, Category
from common.permissions import isOwnerOrReadonly

class TaskModelViewSet(ModelViewSet):
    permission_classes = [isOwnerOrReadonly]
    serializer_class = TaskModelSerializer
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'author', 'status', 'priority']
    search_fields = ['title', 'content', 'author__first_name', 'author___full_name']
    ordering_fields = ['created_date']
    pagination_class = BasePagination

class CategoryViewSet(ModelViewSet):
    permission_classes = [isOwnerOrReadonly]
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()
