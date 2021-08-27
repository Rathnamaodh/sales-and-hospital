from django.contrib.auth.models import User
from rest_framework.test import APIClient
# from rest_framework_simplejwt.tokens import RefreshToken,AccessToken

import pytest


@pytest.fixture()
def my_client():
    hospital = {"hospital": "BBC Hospital","mobile": 8464055655}
    client = APIClient()
    # refresh = RefreshToken.for_user(user)
    # client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    return client