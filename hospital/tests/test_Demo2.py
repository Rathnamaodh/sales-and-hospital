# # from rest_framework.test import RequestsClient

# # client = RequestsClient()
# # response = client.get('http://127.0.0.1:8000/hospital/list')
# # assert response.status_code == 200


# from rest_framework.test import RequestsClient

# client = RequestsClient()
# response = client.get('http://testserver/users/')
# assert response.status_code == 200


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# from myproject.apps.core.models import Account
from cartapp.models import Hospital

class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('hospital_list')
        data = {'name': 'DabApps','mobile': 846800258}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Hospital.objects.count(), 1)
        self.assertEqual(Hospital.objects.get().name, 'DabApps')
        self.assertEqual(Hospital.objects.get().mobile, 846800258)
