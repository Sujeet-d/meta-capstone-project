from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        # Create a temporary test instance
        item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        
        # Verify if the string format matches your expected template
        self.assertEqual(str(item), "IceCream : 80")