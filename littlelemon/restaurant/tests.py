from django.test import TestCase
from .models import Menu

class MenuTest(TestCase):
    def test_menu_item_creation(self):
        item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(item.Title, "IceCream")
        self.assertEqual(item.Price, 80)
        self.assertEqual(item.Inventory, 100)
