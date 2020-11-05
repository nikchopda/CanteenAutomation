from django.test import TestCase
from client.models import Customer
import sys

# Create your tests here.
class ClientTestCase(TestCase):

    def _init_(self):
        self.credentials_positive = {
            'unm': 'artivekaria',
            'pwd': 'arti@123'}

        self.credentials_negative = {
            'unm': 'chopda',
            'pwd': '1234567'}

    def setup(self):
        Customer.objects.create(**self.credentials_positive)
        Customer.objects.create(**self.credentials_negative)

    def test_login_Positive(self):
        # login_with_True_credentials
        response = self.Customer.post('loginvalidation/', **self.credentials_positive)
        self.assertTrue(response.context['/client/choose.html'].is_active)


    def test_login_Negative(self):
         # login_with_False_credentials
         response = self.Customer.post('loginvalidation/', **self.credentials_negative)
         self.assertFalse(response.context['/login.html'].is_active)