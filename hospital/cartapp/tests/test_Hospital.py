from mixer.backend.django import mixer
import pytest
from django.urls import reverse
from cartapp.models import Hospital
from django.test import RequestFactory 
from django.test import Client
from rest_framework.test import APIClient
from cartapp.views import hospital_list
@pytest.mark.django_db
class TestHospitalView:
    def setUp(self):
        self.client = APIClient()

    def test_get_hospital(self,rf, my_client):
        mixer.blend('cartapp.Hospital')
        #request = rf.get(reverse('viewall'))
        print('---------')
        client = APIClient()
        response=my_client.get(reverse('hospital_list'))
        print(response)
        assert  response.status_code == 200


    def test_hospital_list(self,my_client):
        mixer.blend('cartapp.Hospital')
        print('====')
        factory = RequestFactory()
        client = APIClient()
        student = mixer.blend(Hospital, hospital="Rk Hospital",number=8545854545)
        print(student)
        url = reverse("hospital_list")
        response =client.get(url)
        assert response.json() != None
        assert response.status_code == 200

    def test_hospital_create(self):
        # data
        print("Create method...............")
        input_data = {"hospital": "BBC Hospital","mobile": 8464055655}

     
        url = reverse("hospital_list")
        client = APIClient()


        # call the url
        response = client.post(url, data=input_data)

        print("post data",response.data)

        assert response.status_code == 201
        assert Hospital.objects.count() == 1


    def test_hospital_delete(self):
        # create a student
        print("Destroy method................")
        hospital = mixer.blend(Hospital, pk=1, hospital="MkkkkK Hospital", mobile=8464088937)
        assert Hospital.objects.count() == 1

        url = reverse("hospital_detail", kwargs={"pk": 1})
        client = APIClient()
        response = client.delete(url)
        # assertions
        # - json
        # - status

        print(dir(response.json), "response json")
        print((response.status_code), "response json")

        assert response.status_code == 204

        assert Hospital.objects.count() == 0


        













        # #viewmet = PreRegHos(request)
        # sdata=PreRegHos.objects.create(hospital_name="Mediplus",h_address="banjarahills",mobile=9654568125,allocate_to=sdata).save()
        # response=api_client.post(reverse('preghos'),data=sdata)
        # print(response)
        # assert response.status_code == 200


