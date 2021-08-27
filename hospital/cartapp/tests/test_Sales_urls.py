from django.urls import reverse,resolve
from django.test import TestCase

class TestUrls:

    def test_sales_url(self):
        print('hospital url working....')

        path=reverse('sales_list')
        assert resolve(path).view_name == 'sales_list'   

    