from .views.crud import get
from django.urls import path

urlpatterns = [
    path('get/', get.JourneysList.as_view(), name='index')
]