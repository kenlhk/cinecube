from django.test import TestCase
from django.test import Client
import unittest

# Create your tests here.

class LoginMethodsTests(TestCase):

    def test_ensure_login_are_positive(self):
        c = Client()
        response = c.post('/accounts/login/',{'nickname':'shuang','password':'1234567qwe'})
        print(response.status_code)
        self.assertEqual(response.status_code,200)


    def test_ensure_register_are_ositive(self):
        c= Client()
        reponse = c.post('/accounts/register/',{
            'nickname':'testcase',
            'email':'123456@gmail.com',
            'password':'123456',
            'repassword':'123456'
        })
        print(reponse.status_code)

