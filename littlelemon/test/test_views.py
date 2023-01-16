from django.test import TestCase
from django.contrib.auth.models import User

# from rest_framework.authtoken.models import Token

import json
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='jassword')
        self.user.save()

        for menu_id in range(3):
            self.menu_item = Menu.objects.create(
                title=f"Menu {menu_id}",
                price=f"{menu_id * 2}",
                inventory=f"{menu_id * 3}",
            )
            self.menu_item.save()
        menu = Menu.objects.get(title="Menu 1")
        self.assertNotEqual(0, type(menu))
        

    def test_get_all(self):
        self.client.login(username='test', password='jassword')
        response = self.client.get("/api/menu-items/")
        menus = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(menus["results"]), 3)