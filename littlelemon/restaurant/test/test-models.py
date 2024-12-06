from django.test import TestCase
from ..models import Menu

class MenuTest(TestCase):
    def test_menu_item_creation(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.title, "IceCream")
        self.assertEqual(item.price, 80)
        self.assertEqual(item.inventory, 100)
