import pytest
from django.urls import reverse

from tests.base import BaseTest
from .factories import TaskFactory
from tests.accounts.factories import UserFactory
from enums.task import TaskPriority, TaskStatus

class TestTaskAPI(BaseTest):
    
    list_url = reverse('tasks-list')

    @pytest.mark.django_db
    def test_create_object_response_401(self):

        # Arrange
        task = TaskFactory()

        # Act
        response = self.api_client.post(self.list_url)
        
        # Assert
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_create_object_response_201(self):

        # Arrange
        task = TaskFactory.build()
        
        # Act
        self.api_client.force_authenticate(UserFactory())
        response = self.api_client.post(self.list_url, data={
            'title': task.title,
            'content': task.content,
            'status': task.status,
            'priority': task.priority,
        })

        # Assert
        assert response.data.get('title') == task.title
        assert response.status_code == 201
        