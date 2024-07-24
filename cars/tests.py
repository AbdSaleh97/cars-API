from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone

from .models import Car

class CarTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up a test user
        testuser1 = get_user_model().objects.create_user(
            username='test_user',
            email='test@email.com',
            password='1234'
        )

        # Set up a test car
        Car.objects.create(
            buyer=testuser1,
            car_model='Test Model',
            car_brand='Test Brand',
            car_price=10000,
            is_bought=True,
            buy_time=timezone.now()
        )

    def test_str_method(self):
        car = Car.objects.get(id=1)
        self.assertEqual(str(car), 'Test Model')

    def test_car_content(self):
        car = Car.objects.get(id=1)
        self.assertEqual(car.buyer.username, 'test_user')
        self.assertEqual(car.car_model, 'Test Model')
        self.assertEqual(car.car_brand, 'Test Brand')
        self.assertEqual(car.car_price, 10000)
        self.assertTrue(car.is_bought)
