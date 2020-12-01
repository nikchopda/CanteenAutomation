from django.test import TestCase
from prog.models import Admin
import sys

# Create your tests here.
class ProgTestCase(TestCase):

    def _init_(self):
        self.credentials_positive = {
            'email': 'admin@gmail.com',
            'password': 'admin'}

        self.credentials_negative = {
            'name': 'admin@gmail.com',
            'value': '1234567'}

    def setup(self):
        Admin.objects.create(**self.credentials_positive)
        Admin.objects.create(**self.credentials_negative)

    def prog_test_login_Positive(self):
        # login_with_True_credentials
        response = self.Admin.post('adminloginvalidation/', **self.credentials_positive)
        self.assertTrue(response.context['/adminwork.html'].is_active)


    def prog_test_login_Negative(self):
         # login_with_False_credentials
         response = self.Admin.post('adminloginvalidation/', **self.credentials_negative)
         self.assertFalse(response.context['/adminlogin.html'].is_active)