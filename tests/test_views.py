from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    
    def setUp(self) -> None:
        test_item1 = Menu.objects.create(title="IceCream", price=80, inventory=1)
        test_item2 = Menu.objects.create(title="Pizza", price=10, inventory=1)

    def test_getall(self):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        test_items = [
            {
                "id": 2,
                "title": "IceCream",
                "price": "80.00",
                "inventory": 1
            },
            {
                "id": 3,
                "title": "Pizza",
                "price": "10.00",
                "inventory": 1
            }
        ]
        self.assertEqual(serializer.data, test_items)
