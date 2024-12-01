from django.test import TestCase
from journey.models import Journey
from car.models import Car
from users.models import User
from datetime import datetime

class TestJouneyApp (TestCase) :

    def create_user(self, email='test@gmail.com', full_name='test'):
        return User.objects.create(
            email=email,
            full_name=full_name,
            password='123'
        )
        
    def setUp(self) -> None:
        self.get_journey_endpoint = '/journey/get/'
        
    def test_get_sucess_endpoint_and_empty(self) :
        response = self.client.get(self.get_journey_endpoint)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 0)

    def test_get_data(self) :
        driver_user = self.create_user()
        Car.objects.create(
            driver=driver_user,
            car_id='123',
            car_name='test car name',
            max_users=2
        )

        rider_1 = self.create_user('test2@gmail.com','test2')

        jour = Journey.objects.create(
          driver=driver_user,
          from_place='p1',
          to_place='p2',
          start_at=datetime.now(),
        )

        jour.riders.add(rider_1)

        jour.save()

        response = self.client.get(self.get_journey_endpoint+"?from=p1&to=p2")
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.json()), 0)
        
         