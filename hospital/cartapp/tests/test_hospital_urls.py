from django.urls import reverse,resolve
from django.test import TestCase

class TestUrls:

    def test_hospital_url(self):
        print('hospital url working....')

        path=reverse('hospital_list')
        assert resolve(path).view_name == 'hospital_list'   

    