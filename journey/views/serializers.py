from journey.models import Journey
from rest_framework import serializers
from car.models import Car

class JourneySerializer (serializers.ModelSerializer) : 
    
    class Meta:
        model = Journey
        fields = '__all__'

    def to_representation(self, instance:Journey):
        data = super().to_representation(instance)
        driver = instance.driver
        driver_car = Car.objects.get(driver=driver)

        data['driver'] = {
            'full_name' : driver.full_name,
            'picture' : driver.picture.url if driver.picture else None,
        }

        data['passengers_count'] = instance.riders.count(),
        
        car_riders = [i.full_name for i in instance.riders.all()]

        data['car'] = {
            'max_passengers_count' : driver_car.max_users,
            'car_name' : driver_car.car_name,
            'car_id' : driver_car.car_id,
            'riders' : car_riders
        }

        del data['riders']
        return data