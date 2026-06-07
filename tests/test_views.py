from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Initialize the API client wrapper
        self.client = APIClient()
        
        # Set up sample database records for testing
        Menu.objects.create(Title="Bruschetta", Price=6.99, Inventory=50)
        Menu.objects.create(Title="Greek Salad", Price=8.50, Inventory=30)

    def test_getall(self):
        # Send a GET request to your menu items API endpoint
        response = self.client.get('/restaurant/menu/')
        
        # Fetch the records from the test database and serialize them
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        
        # Assertions to ensure the server responds with 200 OK and matching JSON data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)