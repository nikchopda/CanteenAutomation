from django.test import TestCase
from chef.models import Chef
import sys

# Create your tests here.
class ChefTestCase(TestCase):

    def __init__(self):
        self.credentials_positive = {
            'chefid': '1',
            'chefname': 'ramlal'}

        self.credentials_negative = {
            'chefid': '20',
            'chefname': 'ramlal'}

    def setup(self):
        Chef.objects.create(**self.credentials_positive)
        Chef.objects.create(**self.credentials_negative)

    def test_login_Positive(self):
        # login_with_True_credentials
        response = self.Chef.post('loginvalidation/', **self.credentials_positive)
        self.assertTrue(response.context['/chef/chefwork.html'].is_active)

    def test_login_Negative(self):
         # login_with_False_credentials
         response = self.Chef.post('loginvalidation/', **self.credentials_negative)
         self.assertFalse(response.context['/cheflogin.html'].is_active)
