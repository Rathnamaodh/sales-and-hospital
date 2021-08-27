from mixer.backend.django import mixer
import pytest
from django.urls import reverse
from cartapp.models import Hospital,Salesperson
from django.test import RequestFactory 
from django.test import Client
from rest_framework.test import APIClient
from cartapp.views import hospital_list, sales_view
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestSalesView:




    
   
    def test_hospital_create(self):
        # data
        user = mixer.blend(User, username="admin",mobile=8989898585,emaik='admin@gmail.com')
        print(user.id)
      
        z=user.id

        # input_data = mixer.blend(Salesperson,sales=user,hospital=hospital)
        hospital = mixer.blend(Hospital, hospital="My Hospital",mobile=8989898585)
        # print(hospital)
        zx=hospital.id
        # print(zx,'46465465465465465')
        post_data = {'sales':user.pk,'hospital':zx}
        # print('input_data:',input_data.sales,input_data.hospital)
        client = APIClient()
     
        url = reverse("sales_list")
        print(url)
        response = client.post(url, data=post_data)

        print("post data",response.data)

        assert response.status_code == 201
        assert Hospital.objects.count() == 1

