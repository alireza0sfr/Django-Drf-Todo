from factory.django import DjangoModelFactory
from factory import SubFactory


from tests.accounts.factories import ProfileFactory
from enums.task import TaskPriority, TaskStatus
from tests.base import BaseFactory


class CategoryFactory(DjangoModelFactory, BaseFactory):
    name = 'test-category'

    class Meta:
        model = 'task.Category'


class TaskFactory(DjangoModelFactory, BaseFactory):
        
    author = SubFactory(ProfileFactory)
    title = 'test-title'
    content = 'test-content'
    status = TaskStatus.PUBLISHED
    category = SubFactory(CategoryFactory)
    priority = TaskPriority.LOW

    class Meta:
        model = 'task.Task'