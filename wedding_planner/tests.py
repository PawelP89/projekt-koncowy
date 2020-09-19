from django.test import TestCase
from django.urls import reverse
from wedding_planner.views import *

# Create your tests here.


class TestLoginRequired(TestCase):
    def test_redirects_to_login_page_on_not_logged_in(self):
        response = self.client.get(reverse(Podsumowanie))
        self.assertEqual(response.status_code, 303)
        self.assertRedirects(response, reverse('login'))

