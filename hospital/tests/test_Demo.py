import pytest
from cartapp.models import Hospital
from mixer.backend.django import mixer
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from django import urls

from rest_framework.test import APITestCase


# from django.contrib.auth.models import AnonymousUser, User
# from django.test import RequestFactory
# def test_demo():
#     print("Hello")

@pytest.mark.django_db
class TestHospital(APITestCase):
    def setUp(self):
        self.client = APIClient()

    # def test_view_aut_true(self):
    #     mixer.blend('cartapp.Hospital')
    #     path = reverse('hospital_detail', kwargs={'pk':1})
    #     request = RequestFactory().get(path)
    #     request.user = mixer.blend(User)
    #     response = hospital_detail(request,pk=1)
    #     print(response)
    #     assert response.status_code == 200



    def test_hospital_list(self):
        print("getting all data...............")

        student = mixer.blend(Hospital, hospital="Rk Hospital",number=8545854545)
        print(student)


        url = reverse("hospital_list")
        # print("url data is:",url)

        # call the url
        response = self.client.get(url)

        # print(dir(response), "response")

        # aseertions
        # - json
        # - status
        assert response.json() != None

        assert len(response.json()) == 1

        assert response.status_code == 200

    def test_hospital_create(self):
        # data
        print("Create method...............")
        input_data = {"hospital": "BBC Hospital","mobile": 8464055655}

     
        url = reverse("hospital_list")

        # call the url
        response = self.client.post(url, data=input_data)

        print("post data",response.data)

        assert response.status_code == 201
        assert Hospital.objects.count() == 1

    def test_hospital_detail(self):
        # create a hospital
        print("Detail method to get one record ...............")

        hospital = mixer.blend(Hospital, pk=1, hospital="RK Hospital",mobile=8464088937)
        print("hospital id:",hospital.id,"hospital name:",hospital.hospital,"hospital number:",hospital.mobile)
        print(Hospital.objects.last().pk, "data")
        url = reverse("hospital_detail", kwargs={"pk": 1})
        response = self.client.get(url)

        # student2 = mixer.blend(Hospital, pk=2, name="GK Hospital",mobile=8958758758)
        # url2 = reverse("student_detail_api", kwargs={"pk": 2})
        # response2 = self.client.get(url2)

        # assertions
        # - json
        # - status

        print(response.json(), "response json")

        assert response.json() != None
        assert response.status_code == 200
        assert response.json()["hospital"] == "RK Hospital"
        assert response.json()["mobile"] == 8464088937

        # assert response2.json()["hospital"] == "GK Hospital"
        # assert response2.json()["mobile"] == 8958758758


    def test_hospital_delete(self):
        # create a student
        print("Destroy method................")
        hospital = mixer.blend(Hospital, pk=1, hospital="MkkkkK Hospital", mobile=8464088937)
        assert Hospital.objects.count() == 1

        url = reverse("hospital_detail", kwargs={"pk": 1})
        response = self.client.delete(url)
        # assertions
        # - json
        # - status

        print(dir(response.json), "response json")
        print((response.status_code), "response json")

        assert response.status_code == 204

        assert Hospital.objects.count() == 0
