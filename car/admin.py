from django.contrib import admin
from .models import Car


@admin.register(Car)
class CarPanel (admin.ModelAdmin) : 
    list_display = ['driver','car_name','max_users']