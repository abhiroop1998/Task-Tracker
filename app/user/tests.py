from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


# Create your tests here.
class UserRegisterTest(APITestCase):

    def test_create_user(self):
        url = reverse('user-create')

        data = {
            'email': 'superadmin@example.com',
            'password': 'superadmin',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_user_data(self):
        url = reverse('user-create')

        # Test with invalid data (missing required fields)
        data = {
            'email': 'superadmin@example.com',
            # 'password': 'superadmin',  # Missing password
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data['results'])
