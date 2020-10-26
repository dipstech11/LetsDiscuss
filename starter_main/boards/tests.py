from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class HomeTest(TestCase):
    def home_test_view_test(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
