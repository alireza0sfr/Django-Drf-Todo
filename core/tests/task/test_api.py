import pytest

from tests.base import BaseTest
from .factories import TaskFactory
from enums.task import TaskPriority, TaskStatus

class TestTaskAPI(BaseTest):
    
    @pytest.mark.django_db
    def test_new_object(self):

        # Arrange
        task = TaskFactory()

        # Assert
        # assert task.author.first_name == 'john'
        # assert task.title == 'test-title'
        # assert task.content == 'test-content'
        # assert task.status == TaskStatus.PUBLISHED
        # assert task.priority == TaskPriority.LOW
        # assert task.category.name == 'test-category'
        