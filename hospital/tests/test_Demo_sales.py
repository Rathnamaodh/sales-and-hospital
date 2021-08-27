import pytest
from cartapp.models import Hospital
from mixer.backend.django import mixer
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from django import urls
from cartapp.models import Hospital,Salesperson
from django.contrib.auth.models import User

import pytest
from cartapp.models import Hospital
from mixer.backend.django import mixer
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from django import urls

# from django.contrib.auth.models import AnonymousUser, User
# from django.test import RequestFactory
# def test_demo():
#     print("Hello")

@pytest.mark.django_db
class TestHospital(APIClient):
    def setUp(self):
        self.client = APIClient()
    
    def test_hospital_create(self):
        # data
        user = mixer.blend(User, username="admin",mobile=8989898585,emaik='admin@gmail.com')
        print(user.id)
      
        z=user.id

        
      
        # myuser = request.user

        # input_data = mixer.blend(Salesperson,sales=user,hospital=hospital)
        hospital = mixer.blend(Hospital, hospital="My Hospital",mobile=8989898585)
        print(hospital)
        zx=hospital.id
        print(zx,'46465465465465465')
        post_data = {'sales':user.pk,'hospital':zx}
        # print('input_data:',input_data.sales,input_data.hospital)

     
        url = reverse("sales_list")
        print(url)
        response = self.client.post(url, data=post_data)

        # # # call the url
        # # response = self.client.post(url, data=student)
        # # response = self.client.post(url, data=input_data)
        # print("my response",response)

        print("post data",response.data)

        assert response.status_code == 201
        assert Hospital.objects.count() == 1







# @pytest.mark.django_db
# class TestHospital(TestCase):
#     def setUp(self):
#         self.client = APIClient()

    # def test_hospital_list(self):
    #     print("getting all data...............")

    #     sales = mixer.blend(Salesperson)
    #     # print(sales.name,sales.mobile)


    #     url = reverse("sales_list")
    #     # print("url data is:",url)

    #     # call the url
    #     response = self.client.get(url)

    #     # print(dir(response), "response")

    #     # aseertions
    #     # - json
    #     # - status
    #     assert response.json() != None

    #     assert len(response.json()) == 1

    #     assert response.status_code == 200

    # def test_hospital_create(self):
    #     # data
    #     print("Create method...............")
    #     input_data = {'id': 1,'user':"admin","hospital":1}

     
    #     url = reverse("sales_list")
    #     print(url)

    #     # call the url
    #     response = self.client.post(url, data=input_data)

    #     print("post data",response.data)

        # assert response.status_code == 201
        # assert Hospital.objects.count() == 1

    # def test_hospital_detail(self):
    #     # create a hospital
    #     print("Detail method to get one record ...............")

    #     hospital = mixer.blend(Hospital, pk=1, name="RK Hospital",mobile=8464088937)
    #     print("hospital id:",hospital.id,"hospital name:",hospital.name,"hospital number:",hospital.mobile)
    #     print(Hospital.objects.last().pk, "data")
    #     url = reverse("hospital_detail", kwargs={"pk": 1})
    #     response = self.client.get(url)

    #     # student2 = mixer.blend(Hospital, pk=2, name="GK Hospital",mobile=8958758758)
    #     # url2 = reverse("student_detail_api", kwargs={"pk": 2})
    #     # response2 = self.client.get(url2)

    #     # assertions
    #     # - json
    #     # - status

    #     print(response.json(), "response json")

    #     assert response.json() != None
    #     assert response.status_code == 200
    #     assert response.json()["name"] == "RK Hospital"
    #     assert response.json()["mobile"] == 8464088937

    #     # assert response2.json()["name"] == "GK Hospital"
    #     # assert response2.json()["mobile"] == 8958758758


    # def test_hospital_delete(self):
    #     # create a student
    #     print("Destroy method................")
    #     hospital = mixer.blend(Hospital, pk=1, name="MkkkkK Hospital", mobile=8464088937)
    #     assert Hospital.objects.count() == 1

    #     url = reverse("hospital_detail", kwargs={"pk": 1})
    #     response = self.client.delete(url)
    #     # assertions
    #     # - json
    #     # - status

    #     print(dir(response.json), "response json")
    #     print((response.status_code), "response json")

    #     assert response.status_code == 204

    #     assert Hospital.objects.count() == 0
