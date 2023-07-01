from factory.django import DjangoModelFactory


from tests.accounts.factories import ProfileFactory
from enums.task import TaskPriority, TaskStatus
from tests.base import BaseFactory
from task.models import Category, Task


class CategoryFactory(DjangoModelFactory, BaseFactory):
    name = 'test-category'

    class Meta:
        model = Category


class TaskFactory(DjangoModelFactory, BaseFactory):
        
    author = ProfileFactory.build()
    title = 'test-title'
    content = 'test-content'
    status = TaskStatus.PUBLISHED
    category = CategoryFactory.build()
    priority = TaskPriority.LOW

    class Meta:
        model = Task