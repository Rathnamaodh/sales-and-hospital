from mixer.backend.django import mixer
from django.contrib.auth.models import User, AnonymousUser
import pytest
from django.urls import reverse
from cartapp.views import hospital_detail
from django.test import RequestFactory
from cartapp.models import Hospital, Salesperson


@pytest.mark.django_db
class TestViews:
    def test_view_aut_true(self):
        mixer.blend('cartapp.Hospital')
        path = reverse('hospital_detail', kwargs={'pk':1})
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)
        response = hospital_detail(request,pk=1)
        print(response)
        assert response.status_code == 200

    # def test_view_aut_false(self):
    #     mixer.blend('collegeapp.Product')
    #     path = reverse('detail', kwargs={'pk':1})
    #     request = RequestFactory().get(path)
    #     request.user = AnonymousUser()
    #     response = product_detail(request,pk=1)
    #     print(response)
    #     assert response.status_code == 200