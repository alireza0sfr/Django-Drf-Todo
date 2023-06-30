import pytest 
from django.urls import reverse
import json
from model_bakery import baker

from task.models import Task
from tests.base import BaseTest
from tests.fixtures import GlobalFixtures

# @pytest.mark.django_db
# class TestTaskAPI(BaseTests):
    # sample_task = {
    #     'author': 
    #     'title': 'test-title',
    #     'content': 'test-content',

    # }
    # list_url = reverse('tasks-list')
    # detail_url = reverse('tasks-detail')

    # def test_create_task_response_200(self):
    #     response = self.client.get(self.list_url)
        # assert response.status_code == 401

    # def test_get_list_response_401(self):
    #     response = self.client.get(self.list_url)
    #     assert response.status_code == 401

    # def test_get_list_response_200(self, GlobalFixtures):
    #     user = GlobalFixtures.get('user')
    #     self.client.force_authenticate(user)
    #     response = self.client.get(self.list_url)
    #     assert response.status_code == 200

class TestCurrencyEndpoints(BaseTest):

    endpoint = '/api/v1.0/tasks/'

    def test_list(self, api_client):
        baker.make(Task, _quantity=3)

        response = api_client().get(
            self.endpoint
        )

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3

    # def test_create(self, api_client):
    #     currency = baker.prepare(Currency) 
    #     expected_json = {
    #         'name': currency.name,
    #         'code': currency.code,
    #         'symbol': currency.symbol
    #     }

    #     response = api_client().post(
    #         self.endpoint,
    #         data=expected_json,
    #         format='json'
    #     )

    #     assert response.status_code == 201
    #     assert json.loads(response.content) == expected_json

    # def test_retrieve(self, api_client):
    #     currency = baker.make(Currency)
    #     expected_json = {
    #         'name': currency.name,
    #         'code': currency.code,
    #         'symbol': currency.symbol
    #     }
    #     url = f'{self.endpoint}{currency.id}/'

    #     response = api_client().get(url)

    #     assert response.status_code == 200
    #     assert json.loads(response.content) == expected_json

    # def test_update(self, rf, api_client):
    #     old_currency = baker.make(Currency)
    #     new_currency = baker.prepare(Currency)
    #     currency_dict = {
    #         'code': new_currency.code,
    #         'name': new_currency.name,
    #         'symbol': new_currency.symbol
    #     } 

    #     url = f'{self.endpoint}{old_currency.id}/'

    #     response = api_client().put(
    #         url,
    #         currency_dict,
    #         format='json'
    #     )

    #     assert response.status_code == 200
    #     assert json.loads(response.content) == currency_dict

    # @pytest.mark.parametrize('field',[
    #     ('code'),
    #     ('name'),
    #     ('symbol'),
    # ])
    # def test_partial_update(self, mocker, rf, field, api_client):
    #     currency = baker.make(Currency)
    #     currency_dict = {
    #         'code': currency.code,
    #         'name': currency.name,
    #         'symbol': currency.symbol
    #     } 
    #     valid_field = currency_dict[field]
    #     url = f'{self.endpoint}{currency.id}/'

    #     response = api_client().patch(
    #         url,
    #         {field: valid_field},
    #         format='json'
    #     )

    #     assert response.status_code == 200
    #     assert json.loads(response.content)[field] == valid_field

    # def test_delete(self, mocker, api_client):
        currency = baker.make(Currency)
        url = f'{self.endpoint}{currency.id}/'

        response = api_client().delete(url)

        assert response.status_code == 204
        assert Currency.objects.all().count() == 0