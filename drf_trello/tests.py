from rest_framework.test import APITestCase
from django.urls import reverse, path, include
from rest_framework import status
from trello_app.models import Board
from users.models import CustomUser


class BoardTestCase(APITestCase):
    def test_get_board(self):
        response = self.client.get(reverse('api_boards'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_column(self):
        data = {
            "title": "board1",
        }
        response = self.client.post(reverse('api_boards'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ColumnTests(APITestCase):
    def test_create_column(self):
        url = reverse('api_columns')
        data = {
            "id": 1,
            "title": "column2",
            "board": 4
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_get_column(self):
        response = self.client.get(reverse('api_columns'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
