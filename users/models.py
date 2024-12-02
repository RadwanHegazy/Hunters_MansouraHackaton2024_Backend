from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserObjects (BaseUserManager) :
    def create_user (self, password, **fields) : 
        user = self.model(**fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, **fields) :
        fields['is_staff'] = True
        fields['is_superuser'] = True 
        return self.create_user(**fields)
    

class User (AbstractUser) : 

    class UserRole :
        rider = 'rider'
        car_owner = 'car_owner'

    objects = UserObjects()
    username = None
    first_name = None
    last_name = None

    full_name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    picture = models.ImageField(upload_to='user-pics/', null=True, blank=True)
    balance = models.FloatField(default=0)

    role = models.CharField(max_length=10,choices=(
        (UserRole.rider,UserRole.rider),
        (UserRole.car_owner,UserRole.car_owner),
    ))


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self) -> str:
        return self.full_name + f" ( {self.role} )"
    