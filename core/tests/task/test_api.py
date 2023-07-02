import pytest
from django.urls import reverse

from tests.base import BaseTest
from .factories import TaskFactory
from tests.accounts.factories import UserFactory

class TestTaskAPI(BaseTest):
    
    list_url = reverse('tasks-list')

    @pytest.mark.django_db
    def test_create_object_response_401(self):

        # Arrange

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

    @pytest.mark.django_db
    def test_get_object_response_200(self):

        # Arrange
        task = TaskFactory()
        
        # Act
        self.api_client.force_authenticate(UserFactory())
        response = self.api_client.get(reverse('tasks-detail', kwargs={'pk': task.pk}))

        # Assert
        assert response.data.get('title') == task.title
        assert response.data.get('id') == str(task.id)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_put_object_response_200(self):

        # Arrange
        task = TaskFactory()
        
        # Act
        self.api_client.force_authenticate(UserFactory())
        response = self.api_client.put(reverse('tasks-detail', kwargs={'pk': task.pk}), 
                                        data={
                                            'title': 'updated-title'
                                        })

        # Assert
        assert response.data.get('title') == 'updated-title'
        assert response.data.get('id') == str(task.id)
        assert response.status_code == 200


    @pytest.mark.django_db
    def test_list_object_response_200(self):

        # Arrange
        count = 3
        task = TaskFactory.create_batch(count)
        
        # Act
        self.api_client.force_authenticate(UserFactory())
        response = self.api_client.get(self.list_url)

        # Assert
        assert response.data.get('count') == count
        assert response.status_code == 200
        