from django.test import TestCase
from .models import Client

class ClientTestCase(TestCase):
    def setUp(self):
        Client.objects.create(name='John Doe', email='john@example.com')

    def test_client_created(self):
        client = Client.objects.get(name='John Doe')
        self.assertEqual(client.email, 'john@example.com')
