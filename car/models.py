from django.db import models
from users.models import User

class Car (models.Model) : 
    driver = models.OneToOneField(User, related_name='driver_car',on_delete=models.CASCADE)
    car_id = models.CharField(max_length=10)
    car_name = models.CharField(max_length=225)
    max_users = models.IntegerField()

    def __str__(self) : 
        return self.car_name
